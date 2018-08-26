import sys
sys.path.append("..")  # Adds higher directory to python modules path.

import functools
import concurrent.futures
from peewee import DoesNotExist
from datatype_c import facebook_names, twitter_names, instagram_names, youtube_names, hashtags
from clients.cfacebook import FacebookClient
from clients.ctwitter import TwitterClient
from clients.cinstagram import InstagramClient
from clients.cyoutube import YouTubeClient
from tags.twitter_tags import TwitterTagsClient
from database.models import RawFacebookComments, RawTwitterComments, RawInstagramComments, RawYouTubeComments, RawHashtagComments


def run_client(candidate, client):
    client.start(candidate)
    return client.results


def run_contents(content):
    if content['network'] == 'facebook':
        save_content(content, RawFacebookComments)
    elif content['network'] == 'twitter':
        save_content(content, RawTwitterComments)
    elif content['network'] == 'instagram':
        save_content(content, RawInstagramComments)
    elif content['network'] == 'youtube':
        save_content(content, RawYouTubeComments)


def save_comment(comments, candidate, commentsClass):
    for comment in comments:
        try:
            item = commentsClass.get(commentsClass.hash == comment['hash'])
        except DoesNotExist:
            commentsClass(candidate=candidate, **comment).save(force_insert=True)


def save_content(content, commentsClass):
    for data in content['data']:
        candidate = data['name']
        if 'feed' in data:
            for feed in data['feed']:
                save_comment(feed['comments'], candidate, commentsClass)
        else:
            save_comment(data['comments'], candidate, commentsClass)


def run_hashtag(hashtag, client):
    client.start(hashtag)
    return client.results


def run_save_hashtag(content):
    for data in content['data']:
        hashtag = data['hashtag']
        for comment in data['comments']:
            try:
                item = RawHashtagComments.get(RawHashtagComments.hash == comment['hash'])
            except DoesNotExist:
                RawHashtagComments(hashtag=hashtag, **comment).save(force_insert=True)


if __name__ == '__main__':
    np_posts = 5
    np_comments = 2

    clients = [
        (facebook_names, FacebookClient(np_posts=np_posts, np_comments=np_comments)),
        (twitter_names, TwitterClient(np_posts=np_posts, np_comments=np_comments)),
        (instagram_names, InstagramClient(np_posts=np_posts, np_comments=np_comments)),
        (youtube_names, YouTubeClient(np_posts=np_posts, np_comments=np_comments)),
    ]

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executorProcess:
        tw = TwitterTagsClient(np_posts=15)
        contents = list(executorProcess.map(functools.partial(run_hashtag, client=tw), hashtags))
        list(executorProcess.map(run_save_hashtag, contents, chunksize=5))

    # Executa o selenium para coletar os dados, usamos ProcessPool para abrir 4 janelas ao mesmo tempo
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executorProcess:
        for client in clients:
            contents = list(executorProcess.map(functools.partial(run_client, client=client[1]), client[0]))
            # Depois de todos os dados coletados, esta na hora de salvar na base de dados
            list(executorProcess.map(run_contents, contents, chunksize=5))

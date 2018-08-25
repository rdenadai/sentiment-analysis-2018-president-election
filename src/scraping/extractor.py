import sys
sys.path.append("..")  # Adds higher directory to python modules path.

import concurrent.futures
from peewee import DoesNotExist
from datatype_c import facebook_names, twitter_names, instagram_names, youtube_names
from clients.cfacebook import FacebookClient
from clients.ctwitter import TwitterClient
from clients.cinstagram import InstagramClient
from clients.cyoutube import YouTubeClient
from database.models import RawFacebookComments, RawTwitterComments, RawInstagramComments, RawYouTubeComments


def run_client(client):
    client.start()
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


def save_content(content, commentsClass):
    for data in content['data']:
        candidate = data['name']
        for comment in data['comments']:
            try:
                commentsClass.get(commentsClass.uuid == comment['uuid'])
            except DoesNotExist:
                commentsClass(candidate=candidate, **comment).save(force_insert=True)


if __name__ == '__main__':
    np_posts = 5
    np_comments = 5

    clients = [
        FacebookClient(names=facebook_names, np_posts=np_posts, np_comments=np_comments),
        TwitterClient(names=twitter_names, np_posts=np_posts, np_comments=np_comments),
        InstagramClient(names=instagram_names, np_posts=np_posts, np_comments=np_comments),
        YouTubeClient(names=youtube_names, np_posts=np_posts, np_comments=np_comments)
    ]

    contents = []
    # Executa o selenium para coletar os dados, usamos ProcessPool para abrir 4 janelas ao mesmo tempo
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executorProcess:
        contents = list(executorProcess.map(run_client, clients))
    # Depois de todos os dados coletados, esta na hora de salvar na base de dados
    if len(contents) > 0:
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executorProcess:
            executorProcess.map(run_contents, contents, chunksize=20)

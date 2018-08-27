import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from peewee import DoesNotExist
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
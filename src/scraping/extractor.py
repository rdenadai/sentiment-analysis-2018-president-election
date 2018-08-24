import sys
sys.path.append("..")  # Adds higher directory to python modules path.

import concurrent.futures
from datatype_c import facebook_names, twitter_names, instagram_names, youtube_names
from clients.cfacebook import FacebookClient
from clients.ctwitter import TwitterClient
from clients.cinstagram import InstagramClient
from clients.cyoutube import YouTubeClient
from database.models import FacebookComments, TwitterComments, InstagramComments, YouTubeComments


def run_client(client):
    client.start()
    return client.results


def save_content(content, commentsClass):
    for data in content['data']:
        candidate = data['name']
        for comment in data['comments']:
            query = commentsClass.select().where(commentsClass.uuid == comment['uuid'])
            if query.exists():
                commentsClass(candidate=candidate, **comment).save()


if __name__ == '__main__':
    np_posts = 1
    np_comments = 1

    clients = [
        FacebookClient(names=facebook_names, np_posts=np_posts, np_comments=np_comments),
        #TwitterClient(names=twitter_names, np_posts=np_posts, np_comments=np_comments),
        #InstagramClient(names=instagram_names, np_posts=np_posts, np_comments=np_comments),
        #YouTubeClient(names=youtube_names, np_posts=np_posts, np_comments=np_comments)
    ]

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executorProcess:
        contents = list(executorProcess.map(run_client, clients))
        for content in contents:
            if content['network'] == 'facebook':
                save_content(content, FacebookComments)
            elif content['network'] == 'twitter':
                save_content(content, TwitterComments)
            elif content['network'] == 'instagram':
                save_content(content, InstagramComments)
            elif content['network'] == 'youtube':
                save_content(content, YouTubeComments)


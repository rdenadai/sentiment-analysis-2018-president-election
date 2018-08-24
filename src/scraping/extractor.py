import concurrent.futures
from datatype_c import facebook_names, twitter_names, instagram_names, youtube_names
from clients.cfacebook import FacebookClient
from clients.ctwitter import TwitterClient
from clients.cinstagram import InstagramClient
from clients.cyoutube import YouTubeClient
from ..database.models import FacebookComments, TwitterComments, InstagramComments, YouTubeComments


def run_client(client):
    client.start()
    return client.results


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
                for data in content['data']:
                    candidate = data['name']
                    for comment in data['comments']:
                        exist = FacebookComments.get(FacebookComments.uuid == comment['uuid'])
                        if not exist:
                            FacebookComments(candidate=candidate, **comment).save()
            elif content['network'] == 'twitter':
                pass
            elif content['network'] == 'instagram':
                pass
            elif content['network'] == 'youtube':
                pass


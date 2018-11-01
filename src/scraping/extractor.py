import functools
import concurrent.futures
import time

from datatype_c import facebook_names, twitter_names, instagram_names, youtube_names, hashtags
from clients.cfacebook import FacebookClient
from clients.ctwitter import TwitterClient
from clients.cinstagram import InstagramClient
from clients.cyoutube import YouTubeClient
from tags.twitter_tags import TwitterTagsClient
from utils import *


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executorProcess:
        hashtags = [hashtags[i:i+5] for i in range(0, len(hashtags), 5)]
        for hashtag in hashtags:
            start_time = time.time()
            tw = TwitterTagsClient(np_posts=40)
            contents = list(executorProcess.map(functools.partial(run_hashtag, client=tw), hashtag, chunksize=5))
            list(executorProcess.map(run_save_hashtag, contents, chunksize=25))
            print(f'{hashtag} --- {round(time.time() - start_time, 2)} seconds ---')

    np_posts = 4
    np_comments = 4

    clients = [
        (facebook_names, FacebookClient(np_posts=np_posts, np_comments=np_comments)),
        (twitter_names, TwitterClient(np_posts=np_posts, np_comments=np_comments)),
        (instagram_names, InstagramClient(np_posts=np_posts, np_comments=np_comments)),
        (youtube_names, YouTubeClient(np_posts=1, np_comments=2)),
    ]

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executorProcess:
        for client in clients:
            start_time = time.time()
            contents = list(executorProcess.map(functools.partial(run_client, client=client[1]), client[0]))
            # Depois de todos os dados coletados, esta na hora de salvar na base de dados
            list(executorProcess.map(run_contents, contents, chunksize=25))
            print(f'{client.__class__.__name__} --- {round(time.time() - start_time, 2)} seconds ---')

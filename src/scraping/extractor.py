import functools
import concurrent.futures

from datatype_c import facebook_names, twitter_names, instagram_names, youtube_names, hashtags
from clients.cfacebook import FacebookClient
from clients.ctwitter import TwitterClient
from clients.cinstagram import InstagramClient
from clients.cyoutube import YouTubeClient
from tags.twitter_tags import TwitterTagsClient
from utils import *


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executorProcess:
        tw = TwitterTagsClient(np_posts=35)
        contents = list(executorProcess.map(functools.partial(run_hashtag, client=tw), hashtags))
        list(executorProcess.map(run_save_hashtag, contents, chunksize=10))

    np_posts = 7
    np_comments = 5

    clients = [
        (facebook_names, FacebookClient(np_posts=np_posts, np_comments=np_comments)),
        (twitter_names, TwitterClient(np_posts=np_posts, np_comments=np_comments)),
        (instagram_names, InstagramClient(np_posts=np_posts, np_comments=np_comments)),
        (youtube_names, YouTubeClient(np_posts=2, np_comments=2)),
    ]

    # Executa o selenium para coletar os dados, usamos ProcessPool para abrir 4 janelas ao mesmo tempo
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executorProcess:
        for client in clients:
            contents = list(executorProcess.map(functools.partial(run_client, client=client[1]), client[0]))
            # Depois de todos os dados coletados, esta na hora de salvar na base de dados
            list(executorProcess.map(run_contents, contents, chunksize=10))

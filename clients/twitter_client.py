import logging
import tweepy
from decouple import config


class Twitter:

    def __init__(self):
        # == OAuth Authentication ==
        #
        # This mode of authentication is the new preferred way
        # of authenticating with Twitter.

        # The consumer keys can be found on your application's Details
        # page located at https://dev.twitter.com/apps (under "OAuth settings")
        consumer_key = config('TWITTER_CONSUMER_API', default='')
        consumer_secret = config('TWITTER_CONSUMER_SECRET', default='')

        # The access tokens can be found on your applications's Details
        # page located at https://dev.twitter.com/apps (located
        # under "Your access token")
        access_token = config('TWITTER_ACCESS_TOKEN', default='')
        access_token_secret = config('TWITTER_ACCESS_TOKEN_SECRET', default='')

        self.auth = None
        self.api = None
        try:
            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except Exception as e:
            logging.info(f'Error {e}')

    def search(self, query, page=1):
        if self.api:
            tweets = self.api.search(q=query, page=page)
            for tweet in tweets:
                logging.info(tweet)
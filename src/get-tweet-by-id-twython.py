from twython import Twython

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""
twitter = Twython(
    CONSUMER_KEY, CONSUMER_SECRET,
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

id_of_tweet = 387164512995930113
tweet = twitter.show_status(id=id_of_tweet)
print(tweet['text'])
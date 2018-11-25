import csv
import tweepy
import re

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

with open('Portuguese_Twitter_sentiment.csv') as csvfiler:
    readCSV = csv.reader(csvfiler, delimiter=',')
    for row in readCSV:       
        try:
            tweet = api.get_status(row[0])
            # Substitui as ocorrências de nova linha por um único espaço
            info1 = row[0] + '|' + re.sub('\n+', ' ', tweet.text) 
            print(info1)            
        except tweepy.TweepError as err:
            #info2 = row[0] + '|' + err.response.text
            info2 = row[0] + '|' + 'Erro'
            print(info2)

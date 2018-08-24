from decouple import config
from peewee import *


db = SqliteDatabase(config('DATABASE_NAME', default='sentiment_analysis.db'))


class SmallComments(Model):
    uuid = UUIDField(primary_key=True, unique=True, index=True)
    candidate = CharField(max_length=150, index=True)
    username = CharField(max_length=255)
    comment = TextField()

    class Meta:
        database = db


class DefaultComments(SmallComments):
    data = CharField(max_length=50)
    timestamp = TimestampField(resolution=100)

    class Meta:
        database = db


class FacebookComments(DefaultComments):
    class Meta:
        database = db
        table_name = 'facebook_comments'


class TwitterComments(DefaultComments):
    class Meta:
        database = db
        table_name = 'twitter_comments'


class InstagramComments(SmallComments):
    class Meta:
        database = db
        table_name = 'instagram_comments'


class YouTubeComments(SmallComments):
    class Meta:
        database = db
        table_name = 'youtube_comments'

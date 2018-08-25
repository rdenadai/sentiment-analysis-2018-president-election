from peewee import *
from .conn import db


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


class RawFacebookComments(DefaultComments):
    class Meta:
        database = db
        table_name = 'raw_facebook_comments'


class RawTwitterComments(DefaultComments):
    class Meta:
        database = db
        table_name = 'raw_twitter_comments'


class RawInstagramComments(SmallComments):
    class Meta:
        database = db
        table_name = 'raw_instagram_comments'


class RawYouTubeComments(SmallComments):
    class Meta:
        database = db
        table_name = 'raw_youtube_comments'

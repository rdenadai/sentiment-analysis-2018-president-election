from peewee import *
from .conn import db


class SmallComments(Model):
    hash = CharField(primary_key=True, unique=True, index=True, max_length=255)
    candidate = CharField(max_length=150, index=True)
    username = CharField(max_length=255)
    comment = TextField()
    clean_comment = TextField(default='')
    sanitized_comment = TextField(default='')
    emotion = CharField(max_length=255, default='')
    emotion_prob = CharField(max_length=255, default='')
    valence = CharField(max_length=255, default='')
    valence_prob = CharField(max_length=255, default='')

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


class RawHashtagComments(Model):
    hash = CharField(primary_key=True, unique=True, index=True, max_length=255)
    hashtag = CharField(max_length=150, index=True)
    username = CharField(max_length=255)
    comment = TextField()
    data = CharField(max_length=50)
    timestamp = TimestampField(resolution=100)
    clean_comment = TextField(default='')
    sanitized_comment = TextField(default='')
    emotion = CharField(max_length=255, default='')
    emotion_prob = CharField(max_length=255, default='')
    valence = CharField(max_length=255, default='')
    valence_prob = CharField(max_length=255, default='')

    class Meta:
        database = db
        table_name = 'raw_hashtag_comments'

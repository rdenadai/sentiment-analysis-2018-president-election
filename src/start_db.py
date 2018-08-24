from decouple import config
from peewee import *
from database.models import FacebookComments, TwitterComments, InstagramComments, YouTubeComments


if __name__ == "__main__":
    db = SqliteDatabase(config('DATABASE_NAME', default='sentiment_analysis.db'))
    db.connect()
    db.create_tables([FacebookComments, TwitterComments, InstagramComments, YouTubeComments])

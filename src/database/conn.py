from decouple import config
from peewee import SqliteDatabase


db = SqliteDatabase(config('DATABASE_NAME', default='sentiment_analysis.db'))
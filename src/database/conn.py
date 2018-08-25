from decouple import config
from peewee import SqliteDatabase


db = SqliteDatabase(config('DATABASE_PATH', default='sentiment_analysis.db'))
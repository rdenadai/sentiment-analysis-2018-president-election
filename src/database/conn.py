from decouple import config
from peewee import SqliteDatabase


# db = SqliteDatabase(config('DATABASE_PATH', default='sentiment_analysis.db'))
from playhouse.pool import PooledSqliteExtDatabase

db = PooledSqliteExtDatabase(
    config('DATABASE_PATH', default='sentiment_analysis.db'),
    pragmas=[('journal_mode', 'wal')],
    max_connections=30,
    stale_timeout=3600,
    check_same_thread=False)
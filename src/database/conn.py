from decouple import config
from peewee import SqliteDatabase
from playhouse.pool import PooledSqliteExtDatabase, PooledPostgresqlExtDatabase


# db = SqliteDatabase(config('DATABASE_PATH', default='sentiment_analysis.db'))
db = PooledSqliteExtDatabase(
    config('DATABASE_PATH', default='sentiment_analysis.db'),
    pragmas=[('journal_mode', 'wal')],
    max_connections=50,
    stale_timeout=3600,
    check_same_thread=False)

# Caso utilize-se do postgresql como banco de dados
# db = PooledPostgresqlExtDatabase(
#     'database',
#     max_connections=32,
#     stale_timeout=300,  # 5 minutes.
#     host='localhost',
#     user='username', 
#     password='password')

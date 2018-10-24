from database.conn import db
from database.models import RawFacebookComments, RawTwitterComments, RawInstagramComments, RawYouTubeComments, RawHashtagComments
from peewee import *
from playhouse.migrate import *


if __name__ == "__main__":
    db.connect()
    db.create_tables([
        RawFacebookComments,
        RawTwitterComments,
        RawInstagramComments,
        RawYouTubeComments,
        RawHashtagComments,
    ])

    # Exemplo, caso da necessidade de atualizar alguma tabela
    # with db.atomic():
    #     migrator = SqliteMigrator(db)
    #     migrate(
    #         migrator.add_column('raw_facebook_comments', 'clean_comment', TextField(default='')),
    #         migrator.add_column('raw_twitter_comments', 'clean_comment', TextField(default='')),
    #         migrator.add_column('raw_instagram_comments', 'clean_comment', TextField(default='')),
    #         migrator.add_column('raw_youtube_comments', 'clean_comment', TextField(default='')),
    #         migrator.add_column('raw_hashtag_comments', 'clean_comment', TextField(default='')),
    #     )
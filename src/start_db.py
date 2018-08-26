from database.conn import db
from database.models import RawFacebookComments, RawTwitterComments, RawInstagramComments, RawYouTubeComments, RawHashtagComments


if __name__ == "__main__":
    db.connect()
    db.create_tables([
        RawFacebookComments,
        RawTwitterComments,
        RawInstagramComments,
        RawYouTubeComments,
        RawHashtagComments,
    ])

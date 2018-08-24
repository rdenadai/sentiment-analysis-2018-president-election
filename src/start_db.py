from database.conn import db
from database.models import FacebookComments, TwitterComments, InstagramComments, YouTubeComments


if __name__ == "__main__":
    db.connect()
    db.create_tables([FacebookComments, TwitterComments, InstagramComments, YouTubeComments])

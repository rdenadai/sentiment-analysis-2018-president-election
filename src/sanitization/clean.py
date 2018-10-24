import sys
sys.path.append("..")  # Adds higher directory to python modules path.

import time
import re

from peewee import SQL

from database.conn import db
from database.models import RawFacebookComments, RawTwitterComments, RawInstagramComments, RawYouTubeComments, RawHashtagComments
from ai.utils import tokenizer, clean_up


if __name__ == '__main__':
    models = (
        RawFacebookComments, 
        RawTwitterComments,
        RawInstagramComments,
        RawYouTubeComments,
        RawHashtagComments
    )

    N = 300
    for model in models:
        total = int(model.select().count() / N) + 1
        print(f'Total pag para {model.__name__}: {total}')
        print('-' * 30)
        for tt in range(total):
            with db.atomic():
                # filter?? .where(SQL('length(sanitized_comment) = 0'))
                for row in model.select().paginate(tt, N):
                    if row:
                        comment = row.comment.strip()
                        clean_comment = clean_up(comment).strip()
                        sanitized_comment = tokenizer(clean_comment, clean=True).strip()
                        query = model.update(sanitized_comment=sanitized_comment, clean_comment=clean_comment).where(model.hash == row.hash)
                        query.execute()
                        time.sleep(.35)
                if tt % 10 == 0:
                    print(f'pag. {tt}')

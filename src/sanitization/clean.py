import sys
sys.path.append("..")  # Adds higher directory to python modules path.

import asyncio
import time
import re

import uvloop
from peewee import SQL
from aiomultiprocess import Pool

from database.conn import db
from database.models import RawFacebookComments, RawTwitterComments, RawInstagramComments, RawYouTubeComments, RawHashtagComments
from ai.utils import tokenizer, clean_up


async def run_model_update(model):
    # run filter?? .where(SQL('length(clean_comment) = 0'))
    N = 1000
    total = int(model.select().count() / N) + 1
    print(f'Total pag para {model.__name__}: {total}')
    for tt in range(total):
        start_time = time.time()
        with db.atomic() as txn:
            rows = [(row.hash, row.comment) for row in model.select().paginate(tt, N) if row]
            for hashy, comment in rows:
                clean_comment = clean_up(comment).strip()
                sanitized_comment = tokenizer(clean_comment, clean=False)
                query = model.update(sanitized_comment=sanitized_comment, clean_comment=clean_comment).where(model.hash == hashy)
                query.execute()
            txn.commit()
        print(f'{model.__name__} pag. {tt} --- {round(time.time() - start_time, 2)} seconds ---')
        await asyncio.sleep(.05)


async def main():
    models = (
        RawFacebookComments,
        RawTwitterComments,
        RawInstagramComments,
        RawYouTubeComments,
        RawHashtagComments,
    )

    async with Pool() as pool:
       await pool.map(run_model_update, models)
    # run_model_update(RawHashtagComments)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())

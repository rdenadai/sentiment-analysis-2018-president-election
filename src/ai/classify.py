import sys
sys.path.append("..")  # Adds higher directory to python modules path.

import asyncio
import time
import re
from functools import partial

import uvloop
from peewee import SQL
from aiomultiprocess import Pool

import numpy as np
from sklearn.externals import joblib

from database.conn import db
from database.models import RawFacebookComments, RawTwitterComments, RawInstagramComments, RawYouTubeComments, RawHashtagComments
from ai.utils import tokenizer, clean_up


async def run_ml_update(model, mls):
    emt_tfidf, emt_lsa, emt_ml, val_tfidf, val_lsa, val_ml = mls
    N = 50
    total = int(model.select().count() / N) + 1
    print(f'Total pag para {model.__name__}: {total-1}')
    for tt in range(total):
        start_time = time.time()
        with db.atomic() as txn:
            rows = [(row.hash, row.sanitized_comment) for row in model.select().paginate(tt, N) if row]
            for hashy, comment in rows:
                # Emotions
                X_tfidf = emt_tfidf.transform([comment])
                X_svd = emt_lsa.transform(X_tfidf)
                emotion = emt_ml.predict(X_svd)[0]
                emotion_prob = list(np.round(emt_ml.predict_proba(X_svd)[0] * 100, 2))

                # Valence
                X_tfidf = val_tfidf.transform([comment])
                X_svd = val_lsa.transform(X_tfidf)
                valence = val_ml.predict(X_svd)[0]
                valence_prob = list(np.round(val_ml.predict_proba(X_svd)[0] * 100, 2))

                query = model.update(
                    emotion=emotion,
                    emotion_prob=emotion_prob,
                    valence=valence,
                    valence_prob=valence_prob
                ).where(model.hash == hashy)
                query.execute()
            txn.commit()
        print(f'{model.__name__} pag. {tt} - {total-1} --- {round(time.time() - start_time, 2)} seconds ---')
        await asyncio.sleep(.1)
        # time.sleep(.1)


async def main():


    models = (
        # RawFacebookComments,
        RawTwitterComments,
        RawInstagramComments,
        # RawYouTubeComments,
        RawHashtagComments,
    )

    emt_tfidf, emt_lsa, emt_ml = joblib.load('models/tfidf_emotions.sav'), \
                                 joblib.load('models/lsa_emotions.sav'), \
                                 joblib.load('models/model_emotions.sav')
    val_tfidf, val_lsa, val_ml = joblib.load('models/tfidf_valence.sav'), \
                                 joblib.load('models/lsa_valence.sav'), \
                                 joblib.load('models/model_valence.sav')
    mls = (emt_tfidf, emt_lsa, emt_ml, val_tfidf, val_lsa, val_ml)
    
    async with Pool() as pool:
        await pool.map(partial(run_ml_update, mls=mls), models)
    # for model in models:
    #     run_ml_update(model, mls)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())

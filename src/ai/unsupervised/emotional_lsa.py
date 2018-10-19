import time
from functools import partial
import concurrent.futures
from multiprocessing import Pool
import numpy as np
import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from .emotional_lsa_utils import _transform, _calculate_sentiment_weights


# PERFORMANCE ++
def work(words, dims, u, weights, idx):
    return _calculate_sentiment_weights(words, dims, u, weights, idx)


def _calculate_emotional_state(u, idx, emotion_words, weights, dims):
    with concurrent.futures.ProcessPoolExecutor() as procs:
        f = partial(work, dims=dims, u=u, weights=weights, idx=idx)
        wv = procs.map(f, list(emotion_words.values()))
        return np.asarray(list(wv)).T


class EmotionalLSA:

    def __init__(self, use_tfidf=False, dims=100, language='pt', debug=False):
        self.debug = debug
        self.use_tfidf = use_tfidf
        self.dims = dims
        self.nlp = spacy.load(language)
        self.X = None
        self.weights = None

        self._ldocs = 0
        self._vectorize = None

    def fit(self, documents):
        start_time = time.time()
        self._ldocs = len(documents)
        if self.use_tfidf:
            if self.debug: print('using Tf-Idf...')
            self._vectorize = TfidfVectorizer()
        else:
            if self.debug: print('using Count...')
            self._vectorize = CountVectorizer()
        self.X = self._vectorize.fit_transform(documents)
        self.weights = pd.DataFrame(self.X.toarray().T, index=self._vectorize.get_feature_names())
        if self.debug: print(f'Actual number of features: {self.X.get_shape()[1]}')
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))

    def transform(self, emotion_words):
        np.random.seed(12345)
        start_time = time.time()
        if self.debug: print('Calculating SVD...')
        U, S, V = np.linalg.svd(self.X.toarray().T, full_matrices=False)
        U, V = U[:, :self.dims], V[:self.dims, :]
        self.dims = U.shape[1]
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))
        wv = self._emotional_state(U, emotion_words)
        start_time = time.time()
        if self.debug: print('Calculating final emotional matrix...')
        transformed = _transform(wv, V, emotion_words, self._ldocs)
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))
        return transformed

    def fit_transform(self, documents, emotion_words):
        self.fit(documents)
        return self.transform(emotion_words)

    def _emotional_state(self, U, emotion_words):
        start_time = time.time()
        if self.debug: print('Processing emotional state... this may take a while...')
        idx = {w: i for i, w in enumerate(self.weights.index.get_values())}
        # Vamos processar apenas as palavras que refletem sentimentos que realmente existem em nosso corpus
        lista_palavras = idx.keys()
        for key, values in emotion_words.items():
            emotion_words[key] = list(filter(None, [value if value in lista_palavras else None for value in values]))
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        if self.debug: print('Generating emotional state from lexicon...')
        data = _calculate_emotional_state(U, idx, emotion_words, self.weights, self.dims)
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))
        return data

import time
from functools import partial
import concurrent.futures
from multiprocessing import Pool
import numpy as np
from scipy.linalg import svd as SVD
import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from .emotional_lsa_utils import _transform, _calculate_sentiment_weights


# PERFORMANCE ++
def work(words, rank, u, weights):
    return _calculate_sentiment_weights(words, rank, u, weights)


def _calculate_emotional_state(u, emotion_words, weights, rank):
    with concurrent.futures.ProcessPoolExecutor() as procs:
        f = partial(work, rank=rank, u=u, weights=weights)
        wv = procs.map(f, list(emotion_words.values()))
        return np.asarray(list(wv)).T


class EmotionalLSA:

    def __init__(self, use_tfidf=False, rank=50, language='pt', debug=False):
        self.debug = debug
        self.use_tfidf = use_tfidf
        self.rank = rank
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
        self.X = self._vectorize.fit_transform(documents).toarray()
        # Na tese é informado a remoção disso, mas nos teste não fez tanta diferença
        self.X = np.asarray([x for x in self.X if np.sum(x) > np.max(x)])
        self.weights = pd.DataFrame(self.X.T, index=self._vectorize.get_feature_names())
        if self.debug: print(f'Actual number of features: {self.X.shape[1]}')
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))

    def transform(self, emotion_words):
        np.random.seed(0)
        if self.debug: print('Calculating SVD...')
        start_time = time.time()
        U, S, V = SVD(self.X.T, full_matrices=False, lapack_driver='gesvd')
        self.rank = U.shape[1]
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))
        wv = self._emotional_state(U, emotion_words)
        if self.debug: print('Calculating final emotional matrix...')
        start_time = time.time()
        transformed = _transform(wv, V, emotion_words, self._ldocs)
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))
        return transformed

    def fit_transform(self, documents, emotion_words):
        self.fit(documents)
        return self.transform(emotion_words)

    def _emotional_state(self, U, emotion_words):
        if self.debug: print('Processing emotional state... this may take a while...')
        start_time = time.time()
        # Vamos processar apenas as palavras que refletem sentimentos que realmente existem em nosso corpus
        lista_palavras = [w for i, w in enumerate(self.weights.index.get_values())]
        for key, values in emotion_words.items():
            emotion_words[key] = [value for value in values if value in lista_palavras]
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))
        if self.debug: print('Generating emotional state from lexicon...')
        start_time = time.time()
        data = _calculate_emotional_state(U, emotion_words, self.weights, self.rank)
        if self.debug: print("--- %s seconds ---" % (time.time() - start_time))
        return data

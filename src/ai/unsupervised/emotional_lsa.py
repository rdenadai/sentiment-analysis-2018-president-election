import time
from functools import partial
import concurrent.futures
from multiprocessing import Pool
import numpy as np
from sparsesvd import sparsesvd as SVDS
from scipy.sparse import csc_matrix
import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from .emotional_lsa_utils import _transform, _calculate_sentiment_weights


class EmotionalLSA:

    def __init__(self, use_tfidf=False, rank=100, language='pt', debug=False):
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
        self.X = self._vectorize.fit_transform(documents)
        self.weights = pd.DataFrame(self.X.T.toarray(), index=self._vectorize.get_feature_names())
        self.weights = self.weights.loc[(self.weights.sum(axis=1) > 1)]
        if self.debug: print(f'Actual number of features: {self.X.shape[1]}')
        if self.debug: print('--- %s seconds ---' % (time.time() - start_time))

    def transform(self, emotion_words):
        np.random.seed(0)
        if self.debug: print('Calculating SVD...')
        start_time = time.time()
        X2 = csc_matrix(self.weights, dtype=np.float)
        U, S, V = SVDS(X2, k=min(X2.shape))
        U = U.T
        U, V = U[:, :self.rank], V[:self.rank, :]
        self.rank = max(min(U.shape), min(V.shape))
        if self.debug: print('--- %s seconds ---' % (time.time() - start_time))
        WV = self._emotional_state(U, emotion_words)
        if self.debug: print('Calculating final emotional matrix...')
        start_time = time.time()
        transformed = _transform(WV, V, emotion_words, self._ldocs)
        if self.debug: print('--- %s seconds ---' % (time.time() - start_time))
        return transformed

    def fit_transform(self, documents, emotion_words):
        self.fit(documents)
        return self.transform(emotion_words)

    def _emotional_state(self, U, emotion_words):
        if self.debug: print('Processing emotional state...')
        start_time = time.time()
        # Vamos processar apenas as palavras que refletem sentimentos que realmente existem em nosso corpus
        lista_palavras = [w for i, w in enumerate(self.weights.index.get_values())]
        for key, values in emotion_words.items():
            emotion_words[key] = [value for value in values if value in lista_palavras]
        if self.debug: print('--- %s seconds ---' % (time.time() - start_time))
        if self.debug: print('Generating emotional state from lexicon... this may take a while...')
        start_time = time.time()
        WV = _calculate_sentiment_weights(self.rank, emotion_words, self.weights, U)
        if self.debug: print('--- %s seconds ---' % (time.time() - start_time))
        return WV

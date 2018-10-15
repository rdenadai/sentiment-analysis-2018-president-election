from functools import partial
import concurrent.futures
import numpy as np
import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from .emotional_lsa_utils import _transform


def calculate_sentiment_weights(words, rank, u, weights, idx):
    wv = np.zeros((rank))
    for value in words:
        for i in range(rank):
            indexes = filter(None, [e if value in inx else None for e, inx in enumerate(idx.keys())])
            wv[i] += np.sum([u[index][i] * weights.iloc[index].values for index in indexes])
    return wv / rank


def _calculate_emotional_state(u, idx, emotion_words, weights, rank):
    wv = np.zeros((1, 1))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as procs:
        f = partial(calculate_sentiment_weights, rank=rank, u=u, weights=weights, idx=idx)
        calc_weights = procs.map(f, list(emotion_words.values()), chunksize=25)
        wv = np.array(list(calc_weights))
    return wv.T


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

    def transform(self, emotion_words):
        np.random.seed(12345)
        print('Calculating SVD...')
        U, S, V = np.linalg.svd(self.X.toarray().T, full_matrices=False)
        U, S, V = U[:, :self.rank], np.diag(S)[:self.rank, :self.rank], V[:self.rank, :]
        self.rank = U.shape[1]
        wv = self._emotional_state(U, emotion_words)
        print('Calculating final emotional matrix...')
        return _transform(wv, V, emotion_words, self._ldocs)

    def fit_transform(self, documents, emotion_words):
        self.fit(documents)
        return self.transform(emotion_words)

    def _emotional_state(self, U, emotion_words):
        print('Processing emotional state... this may take a while...')
        idx = {w: i for i, w in enumerate(self.weights.index.get_values())}
        # Vamos processar apenas as palavras que refletem sentimentos que realmente existem em nosso corpus
        lista_palavras = idx.keys()
        for key, values in emotion_words.items():
            emotion_words[key] = list(filter(None, [value if value in lista_palavras else None for value in values]))
        return _calculate_emotional_state(U, idx, emotion_words, self.weights, self.rank)

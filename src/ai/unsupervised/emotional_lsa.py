import numpy as np
import pandas as pd
import spacy
from numba import jit

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@jit(parallel=True)
def _normalization(x, a, b):
    return (2 * b) * (x - np.min(x)) / np.ptp(x) + a


@jit(parallel=True)
def _transform(wv, V, emotion_words, _ldocs):
    dtframe = np.zeros((_ldocs, len(emotion_words.keys())))
    for i in range(0, _ldocs):
        for k, it in enumerate(emotion_words.items()):
            a = [wv[:, k]]
            b = [V.T[i]]
            dtframe[i][k] = cosine_similarity(a, b)
    return np.round(_normalization(dtframe, -100, 100), 2)


def _calculate_emotional_state(U, emotion_words, idx, weights, _ldocs, _SIMPLE):
    wv = np.zeros((_ldocs, len(emotion_words.keys())))
    for i in range(0, _ldocs):
        for k, item in enumerate(emotion_words.items()):
            key, values = item
            for value in values:
                try:
                    if _SIMPLE:
                        index = weights.index.get_loc(value)
                        idx_val = U[index]
                        wv[i][k] += idx_val[i] * weights.iloc[index].values[i]
                    else:
                        weight_sum = []
                        indexes = filter(None, [e if value in inx else None for e, inx in enumerate(idx.keys())])
                        for index in indexes:
                            idx_val = U[index]
                            weight_sum.append(idx_val[i] * weights.iloc[index].values[i])
                        wv[i][k] += np.sum(weight_sum)
                except:
                    pass
    return wv / _ldocs


class EmotionalLSA:

    def __init__(self, use_tfidf=False, language='pt', debug=False):
        self.debug = debug
        self.use_tfidf = use_tfidf
        self.nlp = spacy.load(language)
        self.X = None
        self.weights = None

        self._ldocs = 0
        self._vectorize = None
        self._SIMPLE = True

    def fit(self, documents, ngrams=(1, 2)):
        self._ldocs = len(documents)
        if self.use_tfidf:
            if self.debug: print('Tf-Idf:')
            self._SIMPLE = False
            self._vectorize = TfidfVectorizer(max_df=2.5, sublinear_tf=False, use_idf=True, ngram_range=ngrams)
        else:
            if self.debug: print('Count:')
            self._vectorize = CountVectorizer()
        self.X = self._vectorize.fit_transform(documents)
        self.weights = pd.DataFrame(self.X.toarray().T, index=self._vectorize.get_feature_names())
        if self.debug: print(f'Actual number of features: {self.X.get_shape()[1]}')

    def transform(self, emotion_words):
        U, S, V = np.linalg.svd(self.X.toarray().T, full_matrices=False)
        wv = self._emotional_state(U, emotion_words)
        return _transform(wv, V, emotion_words, self._ldocs)

    def fit_transform(self, documents, emotion_words, ngrams=(1, 2)):
        self.fit(documents, ngrams)
        return self.transform(emotion_words)

    def _emotional_state(self, U, emotion_words):
        print('Processing emotional state... this may take a while...')
        idx = {w: i for i, w in enumerate(self.weights.index.get_values())}
        return _calculate_emotional_state(U, emotion_words, idx, self.weights, self._ldocs, self._SIMPLE)

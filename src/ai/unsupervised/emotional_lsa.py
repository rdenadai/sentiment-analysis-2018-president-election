import numpy as np
import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from .emotional_lsa_utils import _transform, _calculate_emotional_state


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
        predicted = self.transform(emotion_words)
        for i, pred_line in enumerate(predicted):
            mmax, mmin = np.max(pred_line), np.min(pred_line)
            if np.abs(mmin) > mmax:
                predicted[i] = -predicted[i]
        return predicted

    def _emotional_state(self, U, emotion_words):
        print('Processing emotional state... this may take a while...')
        idx = {w: i for i, w in enumerate(self.weights.index.get_values())}
        # Vamos processar apenas as palavras que refletem sentimentos que realmente existem em nosso corpus
        for key, values in emotion_words.items():
            words = []
            for value in values:
                words += list(filter(None, [inx if value in inx else None for e, inx in enumerate(idx.keys())]))
            emotion_words[key] = words
        return _calculate_emotional_state(U, emotion_words, idx, self.weights, self._ldocs)

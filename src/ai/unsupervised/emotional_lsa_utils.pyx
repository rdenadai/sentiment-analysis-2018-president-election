import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from cython.parallel import parallel, prange


def _normalization(x, int a, int b):
    return (2 * b) * (x - np.min(x)) / np.ptp(x) + a


def _transform(wv, V, dict emotion_words, int _ldocs):
    cdef int i
    cdef int k

    dtframe = np.zeros((_ldocs, len(emotion_words.keys())))
    for i in range(0, _ldocs):
        for k, it in enumerate(emotion_words.items()):
            a = [wv[:, k]]
            b = [V.T[i]]
            dtframe[i][k] = cosine_similarity(a, b)
    return np.round(_normalization(dtframe, -100, 100), 2)


def _calculate_emotional_state(U, dict emotion_words, dict idx, weights, int _ldocs, _SIMPLE):
    cdef int i
    cdef int k

    wv = np.zeros((_ldocs, len(emotion_words.keys())))
    for k, values in enumerate(emotion_words.values()):
        for value in values:
            for i in range(_ldocs):
                indexes = list(filter(None, [e if value in inx else None for e, inx in enumerate(idx.keys())]))
                wv[i][k] += sum([U[index][i] * weights.iloc[index].values[i] for index in indexes])
    return wv / _ldocs

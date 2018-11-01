import re

import numpy as np
cimport numpy as np
from sklearn.metrics.pairwise import cosine_similarity


cpdef np.ndarray _normalization(np.ndarray x, int a, int b):
    return (2 * b) * (x - np.min(x)) / np.ptp(x) + a


cpdef np.ndarray _transform(np.ndarray WV, np.ndarray V, dict emotion_words, int size):
    cdef int i
    cdef int k
    cdef int e_size
    cdef double mmax
    cdef double mmin
    cdef np.ndarray[np.double_t, ndim=2] dtframe

    e_size = len(emotion_words.keys())

    dtframe = np.ones((size + 2, e_size))
    dtframe[-1, :] = np.tile([-1], e_size)
    for k in range(e_size):
        for i in range(size):
            dtframe[i][k] = cosine_similarity([WV[k]], [V.T[i, :]])
            mmax, mmin = np.max(dtframe[i]), np.min(dtframe[i])
            if abs(mmin) > mmax:
                dtframe[i] = -dtframe[i]
    return np.round(_normalization(dtframe, -100, 100)[:-2], 2)


cpdef np.ndarray _calculate_sentiment_weights(int rank, dict sentiments, WC, np.ndarray U):
    cdef int k
    cdef np.ndarray[np.double_t, ndim=2] WV

    WV = np.zeros((len(sentiments.keys()), rank))
    for k, values  in enumerate(sentiments.values()):
        for value in values:
            pattern = re.compile(r'\b({})\b'.format(value))
            indexes = [e for e, inx in enumerate(WC.index.values) if pattern.search(inx)]
            if len(indexes) > 0:
                WV[k, :] += [U[index] for index in indexes][0]
    return WV / rank

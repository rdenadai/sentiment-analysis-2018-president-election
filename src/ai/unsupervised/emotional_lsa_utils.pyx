import numpy as np
cimport numpy as np
from sklearn.metrics.pairwise import cosine_similarity


cpdef np.ndarray _normalization(np.ndarray x, int a, int b):
    return (2 * b) * (x - np.min(x)) / np.ptp(x) + a


cpdef np.ndarray _transform(np.ndarray wv, np.ndarray V, dict emotion_words, int _ldocs):
    cdef int i
    cdef int k
    cdef int size
    cdef int e_size
    cdef double mmax
    cdef double mmin
    cdef np.ndarray[np.double_t, ndim=2] dtframe

    size = _ldocs + 2
    e_size = len(emotion_words.keys())

    dtframe = np.ones((size, e_size))
    for i in range(_ldocs):
        for k in range(e_size):
            a, b = [wv[:, k]], [V.T[i]]
            dtframe[i][k] = cosine_similarity(a, b)
        mmax, mmin = np.max(dtframe[i]), np.min(dtframe[i])
        if abs(mmin) > mmax:
            dtframe[i] = -dtframe[i]
    dtframe[size-1] = np.tile([-1], e_size)
    return np.round(_normalization(dtframe, -100, 100), 2)[:size-2, :]


cpdef np.ndarray _calculate_sentiment_weights(list words, int rank, np.ndarray U, weights, dict idx):
    cdef int i
    cdef np.ndarray[np.double_t, ndim=1] wv

    wv = np.zeros((rank))
    for value in words:
        for i in range(rank):
            indexes = [e for e, inx in enumerate(idx.keys()) if value in inx]
            wv[i] += sum([U[index][i] * weights.iloc[index].values[i] for index in indexes])
    return wv / rank


cpdef np.ndarray _calculate_emotional_state(np.ndarray U, dict idx, dict emotion_words, weights, int rank):
    cdef int k
    cdef int i
    cdef list values
    cdef np.ndarray[np.double_t, ndim=2] wv

    wv = np.zeros((rank, len(emotion_words.keys())))
    for k, values in enumerate(emotion_words.values()):
        for value in values:
            for i in range(rank):
                indexes = [e for e, inx in enumerate(idx.keys()) if value in inx]
                wv[i][k] += np.sum([U[index][i] * weights.iloc[index].values[i] for index in indexes])
    return wv / rank

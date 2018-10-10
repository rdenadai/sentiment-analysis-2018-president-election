import codecs
import concurrent.futures
from unicodedata import normalize
import concurrent.futures
from string import punctuation
from functools import lru_cache

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from spacy.lang.pt.lemmatizer import LOOKUP


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def _load_emotion_file_content(emotion, path='dataset/emocoes'):
    with open(f'{path}/{emotion}', 'r') as h:
        words = h.readlines()
    return words


@lru_cache(maxsize=256)
def load_six_emotions(filepath):
    """Ekman, Friesen, and Ellsworth 	Anger, disgust, fear, joy, sadness, surprise"""
    emotion_words = {
        'ALEGRIA': _load_emotion_file_content('alegria', filepath),
        'DESGOSTO': _load_emotion_file_content('desgosto', filepath),
        'MEDO': _load_emotion_file_content('medo', filepath),
        'RAIVA': _load_emotion_file_content('raiva', filepath),
        'SURPRESA': _load_emotion_file_content('surpresa', filepath),
        'TRISTEZA': _load_emotion_file_content('tristeza', filepath),
    }
    for key, values in emotion_words.items():
        for i, word in enumerate(values):
            emotion_words[key][i] = ''.join(
                [remover_acentos(p.strip()) for p in LOOKUP.get(word.lower(), word.lower())])
    return emotion_words


@lru_cache(maxsize=256)
def load_valence_emotions_from_oplexicon(filename):
    """NEUTRAL | POSITIVE | NEGATIVE."""
    spacy_conv = {
        'adj': 'ADJ',
        'n': 'NOUN',
        'vb': 'VERB',
        'det': 'DET',
        'emot': 'EMOT',
        'htag': 'HTAG'
    }

    data = {
        'POSITIVO': [],
        'NEGATIVO': [],
        'NEUTRO': [],
    }
    with codecs.open(filename, 'r', 'UTF-8') as hf:
        lines = hf.readlines()
        for line in lines:
            info = line.lower().split(',')
            if len(info[0].split()) <= 1:
                info[1] = [spacy_conv.get(tag) for tag in info[1].split()]
                word, tags, sent = info[:3]
                if 'HTAG' not in tags and 'EMOT' not in tags:
                    word = remover_acentos(word.replace('-se', '')).strip()
                    word = LOOKUP.get(word, word)
                    sent = int(sent)
                    if sent == 1:
                        data['POSITIVO'] += [word]
                    elif sent == -1:
                        data['NEGATIVO'] += [word]
                    else:
                        data['NEUTRO'] += [word]
    data['POSITIVO'] = sorted(list(set(data['POSITIVO'])))
    data['NEGATIVO'] = sorted(list(set(data['NEGATIVO'])))
    data['NEUTRO'] = sorted(list(set(data['NEUTRO'])))
    return data


@lru_cache(maxsize=256)
def load_valence_emotions_from_sentilex(filename):
    """NEUTRAL | POSITIVE | NEGATIVE."""
    data = {
        'POSITIVO': [],
        'NEGATIVO': [],
        'NEUTRO': [],
    }
    with codecs.open(filename, 'r', 'UTF-8') as hf:
        lines = hf.readlines()
        for line in lines:
            info = line.lower().split('.')
            words = [remover_acentos(word.strip()) for word in info[0].split(',')]
            for word in words:
                word = LOOKUP.get(word, word)
                cdata = info[1].split(';')
                if len(cdata) > 0:
                    sent = [int(k.replace('pol:n0=', '')) if 'pol:n0=' in k else None for k in cdata]
                    sent = list(filter(None.__ne__, sent))
                    if len(sent) >= 1:
                        sent = sent[0]
                        if sent == 1:
                            data['POSITIVO'] += [word]
                        elif sent == -1:
                            data['NEGATIVO'] += [word]
                        else:
                            data['NEUTRO'] += [word]
    data['POSITIVO'] = sorted(list(set(data['POSITIVO'])))
    data['NEGATIVO'] = sorted(list(set(data['NEGATIVO'])))
    data['NEUTRO'] = sorted(list(set(data['NEUTRO'])))
    return data


@lru_cache(maxsize=256)
def _get_stopwords():
    stpwords = stopwords.words('portuguese') + list(punctuation)
    rms = ['um', 'não', 'mais', 'muito']
    for rm in rms:
        del stpwords[stpwords.index(rm)]
    return stpwords


def generate_corpus(documents=None, tokenize=False):
    assert len(documents) > 0
    print('Iniciando processamento...')
    tokenized_docs = documents
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as procs:
        if tokenize:
            print('Executando processo de tokenização das frases...')
            tokenized_docs = procs.map(tokenize_frases, documents, chunksize=25)
            print('Executando processo de remoção das stopwords...')
        tokenized_frases = procs.map(rm_stop_words_tokenized, tokenized_docs, chunksize=25)
        print('Filtro e finalização...')
    print('Finalizado...')
    return list(tokenized_frases)


def tokenize_frases(phrase):
    return word_tokenize(remover_acentos(phrase.lower()))


def rm_stop_words_tokenized(phrase):
    phrase = NLP(remover_acentos(phrase.lower()))
    clean_frase = []
    for palavra in phrase:
        if palavra.pos_ != 'PUNCT':
            palavra = palavra.lemma_
            if palavra not in STOPWORDS and not palavra.isdigit():
                clean_frase.append(palavra)
    return ' '.join(clean_frase)


# GLOBALS
NLP = spacy.load('pt')
STOPWORDS = _get_stopwords()

import codecs
import re
import time
import concurrent.futures
from unicodedata import normalize
from string import punctuation
from functools import lru_cache

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spacy.lang.pt import Portuguese
import emoji


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def _load_emotion_file_content(emotion, path='dataset/emocoes'):
    with open(f'{path}/{emotion}', 'r') as h:
        words = h.readlines()
        for i, word in enumerate(words):
            word = word.replace('\n', '').lower().strip()
            words[i] = tokenizer(word)
            # words[i] = [w.lemma_ for w in NLP(word, disable=['parser'])][0]
    return sorted(list(set(words)))


@lru_cache(maxsize=256)
def load_six_emotions(filepath):
    """Ekman, Friesen, and Ellsworth : anger, disgust, fear, joy, sadness, surprise."""
    emotion_words = {
        'ALEGRIA': _load_emotion_file_content('alegria', filepath),
        'DESGOSTO': _load_emotion_file_content('desgosto', filepath),
        'MEDO': _load_emotion_file_content('medo', filepath),
        'RAIVA': _load_emotion_file_content('raiva', filepath),
        'SURPRESA': _load_emotion_file_content('surpresa', filepath),
        'TRISTEZA': _load_emotion_file_content('tristeza', filepath),
    }
    return emotion_words


@lru_cache(maxsize=256)
def load_3_emotions(filepath):
    """Ekman, Friesen, and Ellsworth : anger, disgust, fear, joy, sadness, surprise."""
    emotion_words = {
        'POSITIVO': _load_emotion_file_content('positivo', filepath),
        'NEGATIVO': _load_emotion_file_content('negativo', filepath),
        'NEUTRO': _load_emotion_file_content('neutro', filepath),
    }
    return emotion_words


@lru_cache(maxsize=256)
def load_valence_emotions(filename_oplexicon, filename_sentilex):
    data = {
        'POSITIVO': [],
        'NEGATIVO': [],
        'NEUTRO': [],
    }

    oplexicon = load_valence_emotions_from_oplexicon(filename_oplexicon)
    sentilex = load_valence_emotions_from_sentilex(filename_sentilex)

    data['POSITIVO'] = oplexicon['POSITIVO'] + sentilex['POSITIVO']
    data['NEGATIVO'] = oplexicon['NEGATIVO'] + sentilex['NEGATIVO']
    data['NEUTRO'] = oplexicon['NEUTRO'] + sentilex['NEUTRO']
    data['POSITIVO'] = sorted(list(set(data['POSITIVO'])))
    data['NEGATIVO'] = sorted(list(set(data['NEGATIVO'])))
    data['NEUTRO'] = sorted(list(set(data['NEUTRO'])))
    return data


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
                    word = tokenizer(word.lower().strip())
                    # word = [w.lemma_ for w in NLP(word.lower().strip(), disable=['parser'])][0]
                    if len(word) > 2:
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
            words = [word.strip() for word in info[0].split(',')]
            for word in words:
                word = tokenizer(word.lower().strip())
                # word = [w.lemma_ for w in NLP(word.lower().strip(), disable=['parser'])][0]
                if len(word) > 2:
                    cdata = info[1].split(';')
                    if len(cdata) > 0:
                        sent0 = [int(k.replace('pol:n0=', '')) if 'pol:n0=' in k else None for k in cdata]
                        sent1 = [int(k.replace('pol:n1=', '')) if 'pol:n1=' in k else None for k in cdata]
                        sent0 = list(filter(None.__ne__, sent0))
                        sent1 = list(filter(None.__ne__, sent1))
                        if len(sent0) >= 1 and len(sent1) <= 0:
                            sent = sent0[0]
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
def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    return True


@lru_cache(maxsize=256)
def _get_stopwords():
    stpwords = stopwords.words('portuguese')
    rms = ['um', 'não', 'mais', 'muito']
    for rm in rms:
        del stpwords[stpwords.index(rm)]
    return stpwords, punctuation


def generate_corpus(documents=None, debug=False):
    assert len(documents) > 0
    if debug: print('Iniciando processamento...')
    tokenized_docs = documents
    with concurrent.futures.ProcessPoolExecutor() as procs:
        if debug: print('Executando processo de remoção das stopwords...')
        tokenized_frases = procs.map(tokenizer, tokenized_docs, chunksize=25)
    if debug: print('Finalizado...')
    return list(tokenized_frases)


def tokenizer(phrase, clean=False):
    if not clean:
        phrase = clean_up(phrase, False)
    clean_frase = []
    clfa = clean_frase.append
    for palavra in phrase:
        palavra = ''.join([word.lemma_ for word in NLP(palavra)])
        clfa(STEMMER.stem(palavra))
    return ' '.join(clean_frase)


def clean_up(phrase, join=True):
    STOPWORDS, PUNCT = _get_stopwords()
    # Transforma as hashtags em palavras
    try:
        for group in re.findall(r'#\S+\b', phrase, re.DOTALL):
            g2 = re.sub(r'([A-Z])', r' \1', group, flags=re.MULTILINE)
            phrase = re.sub(r'{}\b'.format(group), g2, phrase, flags=re.MULTILINE)
    except Exception:
        pass
    # lowercase para fazer outros pre-processamentos
    phrase = phrase.lower()
    phrase = emoji.get_emoji_regexp().sub(r'', phrase)
    for stw in STOPWORDS:
        phrase = re.sub(r'\b{}\b'.format(stw), '', phrase, flags=re.MULTILINE)
    for punct in PUNCT:
        phrase = phrase.replace(punct, ' ')
    for o, r in RM:
        phrase = re.sub(o, r, phrase, flags=re.MULTILINE)

    # Limpeza extra
    phrase = word_tokenize(phrase)
    clean_frase = []
    clfa = clean_frase.append
    for palavra in phrase:
        if not is_number(palavra) and len(palavra) > 2:
            clfa(palavra)
    return ' '.join(clean_frase) if join else clean_frase


# GLOBALS
NLP = Portuguese()
# STEMMER = nltk.stem.RSLPStemmer()
STEMMER = nltk.stem.SnowballStemmer('portuguese')
STOPWORDS, PUNCT = _get_stopwords()
RM = [
    (r'(http[s]*?:\/\/)+.*[\r\n]*', r''), (r'@', r''),
    (r'\n+', r' . '), (r'"', r' '), (r'\'', r' '),
    (r'#', r''), (r'(RT)', r''), (r'[…]', ' . '), (r'[0-9]*', r''),
    (r'“', r''), (r'”', ''), (r'([aeiouqwtyupdfghjklçzxcvbnm|!@$%&\.\[\]\(\)+-_=<>,;:])\1+', r'\1'),
    (r'(\bñ\n)', 'não'), (r'(nã)', 'não'), (r'\s+', r' '), (r'(nãoo)', 'não'),
]

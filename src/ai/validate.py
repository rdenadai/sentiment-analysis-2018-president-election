from utils import load_six_emotions, load_valence_emotions_from_oplexicon, load_valence_emotions_from_sentilex, generate_corpus
from unsupervised.emotional_lsa import EmotionalLSA
import pandas as pd
from nltk.corpus import floresta as flt
from nltk.corpus import machado as mch
from nltk.corpus import mac_morpho as mcm


if __name__ == '__main__':

    with open('/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/frases.txt') as h:
        original_phrases = h.readlines()
    original_phrases = original_phrases
    phrases = generate_corpus(original_phrases)

    ldocs = [f'D{i}' for i in range(len(phrases))]
    print('Loading emotional words: ')
    # emotion_words = load_six_emotions('/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes')
    # emotion_words = load_valence_emotions_from_oplexicon(
    #     '/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes/oplexicon_v3.0/lexico_v3.0.txt')
    emotion_words = load_six_emotions(
        '/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes')
    emotion_words_n = load_valence_emotions_from_sentilex(
        '/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes/SentiLex-PT02/SentiLex-flex-PT02.txt')
    emotion_words['NEUTRO'] = emotion_words_n['NEUTRO']

    print('Starting EmotionalLSA model...')
    model = EmotionalLSA(use_tfidf=True, debug=True)
    print('fit and transform...')
    predicted = model.fit_transform(phrases, emotion_words)

    print('Showing results:')
    print('-' * 40)
    for i, frase in enumerate(original_phrases):
        print(f' D{i} - {frase}')

    df = pd.DataFrame(predicted, index=ldocs, columns=emotion_words.keys())
    print(df)

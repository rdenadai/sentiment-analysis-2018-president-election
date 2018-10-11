from utils import load_six_emotions, load_valence_emotions_from_oplexicon, load_valence_emotions_from_sentilex, generate_corpus
from unsupervised.emotional_lsa import EmotionalLSA
import pandas as pd
from nltk.corpus import floresta as flt
from nltk.corpus import machado as mch
from nltk.corpus import mac_morpho as mcm


if __name__ == '__main__':

    original_phrases = [
        'Quando a tristeza bater na sua porta, abra um belo sorriso e diga: Desculpa, mas hoje a felicidade chegou primeiro!',
        'Feliz é aquele que vê a felicidade dos outros sem ter inveja. O sol é para todos e a sombra pra quem merece.',
        'Minha meta é ser feliz, não perfeito.',
        'Ser feliz até onde der, até onde puder. Sem adiar, ser feliz o tanto que durar.',
        'Nunca deixe ninguém dizer que você não pode fazer alguma coisa. Se você tem um sonho, tem que correr atrás dele. As pessoas não conseguem vencer, e dizem que você também não vai vencer. Se quer alguma coisa, corre atrás.',
        'O maior problema em acreditar nas pessoas erradas, é que um dia você acaba não acreditando em mais ninguém.',
        'Não me deixe ir, posso nunca mais voltar.',
        'Não me arrependo de ter conhecido ninguém, só me arrependo de ter perdido tanto tempo com algumas pessoas.',
        'Se existe uma coisa que eu me arrependo é de ter confiado em algumas pessoas.',
        'Prefiro que enxerguem em mim erros com arrependimento do que uma falsa perfeição.',
        'Mesmo sabendo que um dia a vida acaba, a gente nunca está preparado para perder alguém.',
        'A morte é uma pétala que se solta da flor e deixa uma eterna saudade no coração.',
        'Mãe é imortal, porque quando ela parte para outro mundo fica vivendo nas lágrimas que escorrem em nosso rosto eternamente.',
        'Só existem dois motivos pra uma pessoa se preocupar com você: Ou ela te ama muito, ou você tem algo que ela queira muito!',
        'Ser feliz nao é ter uma vida perfeita, mas sim reconhecer que vale a pena viver apesar de todos os desafios e perdas.',
        'Minha maravilhosa vida é uma merda.'
    ]
    phrases = generate_corpus(original_phrases)

    ldocs = [f'D{i}' for i in range(len(phrases))]
    print('Loading emotional words: ')
    # emotion_words = load_six_emotions('/home/rdenadai/programas/vagrant_img/vagrant.machine.puphpet/projetos/github/sentiment-analysis-2018-president-election/dataset/emocoes')
    # emotion_words = load_valence_emotions_from_oplexicon(
    #     '/home/rdenadai/programas/vagrant_img/vagrant.machine.puphpet/projetos/github/sentiment-analysis-2018-president-election/dataset/emocoes/oplexicon_v3.0/lexico_v3.0.txt')
    emotion_words = load_six_emotions(
        '/home/rdenadai/programas/vagrant_img/vagrant.machine.puphpet/projetos/github/sentiment-analysis-2018-president-election/dataset/emocoes')
    emotion_words_n = load_valence_emotions_from_sentilex(
        '/home/rdenadai/programas/vagrant_img/vagrant.machine.puphpet/projetos/github/sentiment-analysis-2018-president-election/dataset/emocoes/SentiLex-PT02/SentiLex-flex-PT02.txt')
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
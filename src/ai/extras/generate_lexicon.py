from utils import load_valence_emotions

# Este script é apenas para gerar o dataset novo de positivas/negativas/neutras a partir do Oplexicon e SentiLex


if __name__ == '__main__':
    emotion_words_n = load_valence_emotions(
        '/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes/oplexicon_v3.0/lexico_v3.0.txt',
        '/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes/SentiLex-PT02/SentiLex-flex-PT02.txt'
    )

    with open('/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes/positivo', 'w+') as pos:
        for emot in emotion_words_n['POSITIVO']:
            pos.write(f'{emot}\n')
    with open('/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes/negativo', 'w+') as pos:
        for emot in emotion_words_n['NEGATIVO']:
            pos.write(f'{emot}\n')
    with open('/home/rdenadai/vagrant/python-dev/sentiment-analysis-2018-president-election/dataset/emocoes/neutro', 'w+') as pos:
        for emot in emotion_words_n['NEUTRO']:
            pos.write(f'{emot}\n')
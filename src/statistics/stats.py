import datetime
from collections import OrderedDict
import operator

import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud


stpwords = stopwords.words('portuguese')
stpwords += [
    'acabar', 'achei', 'acho', 'acima', 'acinte', 'adrede', 'agora', 'ainda', 'algum', 'alguma', 'alguns', 'alguém', 'ana', 'antes', 'aqui', 'assim', 'bem', 'cara', 'certeza', 'chega', 'coisa', 'coisas', 'colocar', 'como', 'compartilhe', 'conheça', 'conosco', 'contigo', 'continue', 'dar', 'debalde', 'demais', 'dessa', 'desse', 'deu', 'deve', 'deveria', 'dino', 'disse', 'dizer', 'em', 'enquanto', 'então', 'estar', 'facebook', 'falando', 'falar', 'fale', 'falta', 'faz', 'fazendo', 'fazer', 'fez', 'fica', 'ficamos', 'ficar', 'ficou', 'forma', 'geral', 'gostaria', 'htps', 'jair', 'jeito', 'mal', 'maneira', 'meio', 'menos', 'mesma', 'mil', 'modo', 'mostra', 'mostrar', 'muita', 'nada', 'nao', 'neles', 'nessa', 'nesse', 'news', 'nome', 'nova', 'olá', 'onde', 'outra', 'outro', 'outros', 'parece', 'pode', 'podemos', 'pois', 'porque', 'porventura', 'poucos', 'pra', 'precisa', 'pro', 'qualquer', 'quanto', 'querem', 'queria', 'quero', 'realmente', 'sabe', 'saber', 'sei', 'sempre', 'ser', 'sim', 'sobre', 'talvez', 'ter', 'tirar', 'toa', 'toda', 'todas', 'todo', 'todos', 'tão', 'vai', 'vamos', 'vcs', 'vejo', 'vem', 'ver', 'vez', 'vou', 'vão'
]
stpwords += [
    'presidente', 'brasil', 'voto', 'votar', 'turno',
    'bolsonaro', 'hadad', 'ciro', 'geraldo', 'marina', 'alckmin', 'silva', 'gomes', 'jair',
    'geraldoalckmin', 'jairbolsonaro', 'jairmessiasbolsonaro', 'cirogomes',
    'share', 'source', 'igshid', 'eleicoes', 'acaboua'
]


def word_count(query):
    palavras = []
    for i, row in enumerate(query):
        palavras += [word for word in word_tokenize(row.clean_comment) if word not in stpwords]
    return len(palavras)


def word_frequency(query):
    palavras = []
    for i, row in enumerate(query):
        palavras += [word for word in word_tokenize(row.clean_comment) if word not in stpwords]
    return FreqDist(palavras)


def unique_users(query):
    users = dict()
    for i, row in enumerate(query):
        if row.username in users:
            users[row.username] += 1
        else:
            users[row.username] = 1
    users = sorted(users.items(), key=operator.itemgetter(1))
    users.reverse()
    return users


def comments_by_date(query):
    dates = OrderedDict()
    for i, row in enumerate(query):
        dt = datetime.datetime.strftime(datetime.datetime.strptime(row.data, '%d/%m/%Y %H:%M'), '%d/%m/%Y')
        if dt in dates:
            dates[dt] += 1
        else:
            dates[dt] = 1
    return dates


def create_wordcloud(query, max_words=80):
    freq = word_frequency(query)
    wordcloud = WordCloud(background_color="white", max_words=max_words).generate_from_frequencies(freq)

    plt.figure(figsize=(9, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def graph_comment_by_date(dates):
    labels = list(dates.keys())
    x = list(dates.values())
    plt.figure(figsize=(15, 7))
    plt.title("Quantidade de comentários por data")
    plt.plot(labels, x, '-o')
    plt.xticks(rotation=75)
    plt.show()

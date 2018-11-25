from collections import OrderedDict
import copy
import datetime
import operator
from functools import reduce

import numpy as np
from peewee import SQL
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud


stpwords = stopwords.words('portuguese')
stpwords += [
    'acabar', 'achei', 'acho', 'acima', 'acinte', 'adrede', 'agora', 'ainda', 'algum', 'alguma', 'alguns', 'alguém',
    'ana', 'antes', 'aqui', 'assim', 'bem', 'cara', 'certeza', 'chega', 'coisa', 'coisas', 'colocar', 'como',
    'compartilhe', 'conheça', 'conosco', 'contigo', 'continue', 'dar', 'debalde', 'demais', 'dessa', 'desse',
    'deu', 'deve', 'deveria', 'dino', 'disse', 'dizer', 'em', 'enquanto', 'então', 'estar', 'facebook', 'falando',
    'falar', 'fale', 'falta', 'faz', 'fazendo', 'fazer', 'fez', 'fica', 'ficamos', 'ficar', 'ficou', 'forma', 'geral',
    'gostaria', 'htps', 'jair', 'jeito', 'mal', 'maneira', 'meio', 'menos', 'mesma', 'mil', 'modo', 'mostra',
    'mostrar', 'muita', 'nada', 'nao', 'neles', 'nessa', 'nesse', 'news', 'nome', 'nova', 'olá', 'onde', 'outra',
    'outro', 'outros', 'parece', 'pode', 'podemos', 'pois', 'porque', 'porventura', 'poucos', 'pra', 'precisa', 'pro',
    'qualquer', 'quanto', 'querem', 'queria', 'quero', 'realmente', 'sabe', 'saber', 'sei', 'sempre', 'ser', 'sim',
    'sobre', 'talvez', 'ter', 'tirar', 'toa', 'toda', 'todas', 'todo', 'todos', 'tão', 'vai', 'vamos', 'vcs', 'vejo',
    'vem', 'ver', 'vez', 'vou', 'vão', 'querer', 'quer', 'achar', 'fala'
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


def graph_most_words_freq_by_date(model, query, turno=0, candidato=None, most_common=5):
    words = word_frequency(query)

    clauses = [(SQL('length(clean_comment) > 0'))]
    if turno == 1:
        clauses.append((model.timestamp <= datetime.date(2018, 10, 7)))
    elif turno == 2:
        clauses.append((model.timestamp > datetime.date(2018, 10, 7)))
    if candidato:
        clauses.append((model.candidate == candidato))
    expr = reduce(operator.and_, clauses)
    q_dt = model.select().where(expr).order_by(model.timestamp)
    all_dates = OrderedDict()
    for i, row in enumerate(q_dt):
        dt = datetime.datetime.strftime(datetime.datetime.strptime(row.data, '%d/%m/%Y %H:%M'), '%d/%m/%Y')
        all_dates[dt] = 0

    words_freq = []
    words_by_date = []
    commons = words.most_common(most_common)
    for common in commons:
        word = common[0]

        clauses = [
            (SQL('length(clean_comment) > 0')),
            (model.clean_comment.contains(word))
        ]
        if turno == 1:
            clauses.append((model.timestamp <= datetime.date(2018, 10, 7)))
        elif turno == 2:
            clauses.append((model.timestamp > datetime.date(2018, 10, 7)))
        if candidato:
            clauses.append((model.candidate == candidato))
        expr = reduce(operator.and_, clauses)
        query2 = model.select().where(expr).order_by(model.timestamp)

        dates = copy.deepcopy(all_dates)
        for i, row in enumerate(query2):
            dt = datetime.datetime.strftime(datetime.datetime.strptime(row.data, '%d/%m/%Y %H:%M'), '%d/%m/%Y')
            dates[dt] += 1
        words_freq.append(word)
        words_by_date.append(dates)

    plt.figure(figsize=(15, 7))
    plt.title("Quantidade de comentários por data usando as palavras mais frequentes")
    ant = np.zeros((len(words_by_date[0].values())))
    for k, worda in enumerate(words_freq):
        labels = list(words_by_date[k].keys())
        x = list(words_by_date[k].values())
        plt.bar(labels, x, width=0.5, bottom=ant)
        ant += x
    plt.xticks(rotation=90)
    plt.legend(words_freq)
    plt.show()

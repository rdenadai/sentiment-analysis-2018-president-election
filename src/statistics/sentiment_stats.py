import copy
import datetime
from collections import OrderedDict
import operator
from functools import reduce
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_emocoes_comentarios(comentarios_positivos, comentarios_negativos, comentarios_neutros):
    alegria, surpresa, positivo = [], [], []
    for row in comentarios_positivos:
        if row.emotion == 'ALEGRIA':
            alegria.append(row)
        elif row.emotion == 'SURPRESA':
            surpresa.append(row)
        positivo.append(row)

    tristeza, medo, raiva, desgosto, negativo = [], [], [], [], []
    for row in comentarios_negativos:
        if row.emotion == 'TRISTEZA':
            tristeza.append(row)
        elif row.emotion == 'MEDO':
            medo.append(row)
        elif row.emotion == 'RAIVA':
            raiva.append(row)
        elif row.emotion == 'DESGOSTO':
            desgosto.append(row)
        negativo.append(row)

    neutro = []
    for row in comentarios_neutros:
        neutro.append(row)
    return alegria, surpresa, tristeza, medo, raiva, desgosto, positivo, negativo, neutro


def print_statistics(rede_social, total_comentarios, comentarios_positivos, comentarios_negativos, comentarios_neutros):
    total = len(comentarios_positivos) + len(comentarios_negativos) + len(comentarios_neutros)

    print(f'Estatísticas do {rede_social}:')
    print('-' * 20)
    print(f'Total de Comentários  : {total_comentarios}')
    print(f'Comentários Positivos : {len(comentarios_positivos)}')
    print(f'Comentários Negativos : {len(comentarios_negativos)}')
    print(f'Comentários Neutros   : {len(comentarios_neutros)}')
    print()
    print('Porcentagem de comentários:')
    print('-' * 20)
    print(f'Comentários Positivos : {round(len(comentarios_positivos)/total_comentarios * 100, 2)}%')
    print(f'Comentários Negativos : {round(len(comentarios_negativos)/total_comentarios * 100, 2)}%')
    print(f'Comentários Negativos : {round(len(comentarios_neutros)/total_comentarios * 100, 2)}%')
    print(f'Total                 : {round(total/total_comentarios * 100, 2)}%')


def graph_sentimentos_total(rede_social, cores, sentimentos, alegria, surpresa, tristeza, medo, raiva, desgosto, neutro):
    values = np.array([
        [len(alegria)], [len(surpresa)], [len(tristeza)],
        [len(medo)], [len(raiva)], [len(desgosto)], [len(neutro)]
    ])
    df = pd.DataFrame(
        values.T,
        columns=sentimentos
    )

    display(df)

    plt.figure(figsize=(8, 4))
    plt.title(f'Distribuição total das emoções : {rede_social}')
    barlist = plt.bar(sentimentos, df.values[0])
    for k, cor in enumerate(cores):
        barlist[k].set_color(cor)
    plt.show()


def graph_valence_total(rede_social, cores_val, valencia, positivo, negativo, neutro):
    values = np.array([
        [len(positivo)], [len(negativo)], [len(neutro)]
    ])
    df = pd.DataFrame(
        values.T,
        columns=valencia
    )

    display(df)

    plt.figure(figsize=(8, 4))
    plt.title(f'Distribuição total das valências : {rede_social}')
    barlist = plt.bar(valencia, df.values[0])
    for k, cor in enumerate(cores_val):
        barlist[k].set_color(cor)
    plt.show()


def graph_emocoes_por_data(rede_social, cores2, sentimentos_dict, comentarios):
    datas = {}
    for i, row in enumerate(comentarios):
        dt = datetime.datetime.strftime(datetime.datetime.strptime(row.data, '%d/%m/%Y %H:%M'), '%d/%m/%Y')
        datas[dt] = copy.deepcopy(sentimentos_dict)
    for i, row in enumerate(comentarios):
        dt = datetime.datetime.strftime(datetime.datetime.strptime(row.data, '%d/%m/%Y %H:%M'), '%d/%m/%Y')
        datas[dt][row.emotion] += 1

    df = pd.DataFrame(datas, columns=datas.keys())
    display(df.iloc[:, :8])
    df.T.plot.bar(stacked=True, color=cores2, figsize=(17, 6))
    plt.title(f'Emoções por data : {rede_social}')
    plt.show()


def graph_valencia_por_data(rede_social, cores_val, valencia_dict, comentarios):
    datas = {}
    for i, row in enumerate(comentarios):
        dt = datetime.datetime.strftime(datetime.datetime.strptime(row.data, '%d/%m/%Y %H:%M'), '%d/%m/%Y')
        datas[dt] = copy.deepcopy(valencia_dict)
    for i, row in enumerate(comentarios):
        dt = datetime.datetime.strftime(datetime.datetime.strptime(row.data, '%d/%m/%Y %H:%M'), '%d/%m/%Y')
        datas[dt][row.valence] += 1

    df = pd.DataFrame(datas, columns=datas.keys())
    display(df.iloc[:, :8])
    df.T.plot.bar(stacked=True, color=cores_val, figsize=(17, 6))
    plt.title(f'Emoções por data : {rede_social}')
    plt.show()
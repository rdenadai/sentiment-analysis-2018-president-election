import csv
import re

# Expressão regular para identificar URLs (HTTP e HTTPS)
url_http_re = 'http:\/\/(www\.)?.*[^ ]'
url_https_re = 'http[s]:\/\/(www\.)?.*[^ ]'

with open('resultados.csv', encoding='utf-8') as fin:
    readCSV = csv.reader(fin, delimiter='|')
    for row in readCSV:
        # Substitui as ocorrências de nova linha por um único espaço
        row[1] = re.sub('\n+', ' ', row[1])
        # Substitui a ocorrência de URLs (HTTP e HTTPS) por um único espaço
        row[1] = re.sub(url_http_re, ' ', row[1])
        row[1] = re.sub(url_https_re, ' ', row[1])
        # Substitui as ocorrências de espaço duplo por espaço simples
        row[1] = re.sub('  ', ' ', row[1])
        line = row[0] + '|' + row[1]
        print(line)
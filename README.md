# Sentiment Analysis for 2018 President Election

Análise de sentimentos relacionados aos candidatos a Eleição para a presidência de 2018


### Instalação

#### Requisitos

 - python 3.6+
 
> Caso não possua o python 3.6+ (sugiro o 3.7), veja como instalar.
Você pode usar o [pyenv](https://github.com/pyenv/pyenv) para instalar várias versões paralelamente.

 1. Faça o git clone deste repositório;
 2. Execute os seguintes comandos (depois de ter instalado o python 3.6+)
    ```bash
    $> virtualenv venv
    $> pip install -r requirements.txt
    $> source venv/bin/activate
    ```
 3.
    ```bash
    FACEBOOK_USER=
    FACEBOOK_PASSWORD=
    ```
 4. Extraia e copie o conteúdo da pasta **selenium_driver** caso queira executar o passo 4.
 5. Execute o arquivo extractor.py caso queira extrair novamente os dados das redes sociais.
    ```bash
    $> python extractor.py
    ```
 
 
#### Páginas extraídas
1. Instagram
    - [Jair Bolsonaro](https://www.instagram.com/jairmessiasbolsonaro/?hl=pt-br)
    - [Geraldo Alckmin](https://www.instagram.com/geraldoalckmin_/?hl=pt-br)
    - [Fernando Haddad](https://www.instagram.com/fernandohaddadoficial/)
    - [Marina Silva](https://www.instagram.com/_marinasilva_/?hl=pt-br)
    - [Ciro Gomes](https://www.instagram.com/cirogomes/?hl=pt-br)
2. Facebook
    - [Jair Bolsonaro](https://www.facebook.com/jairmessias.bolsonaro/)
    - [Geraldo Alckmin](https://www.facebook.com/geraldoalckmin/)
    - [Fernando Haddad](https://www.facebook.com/fernandohaddad/)
    - [Marina Silva](https://www.facebook.com/marinasilva.oficial/)
    - [Ciro Gomes](https://www.facebook.com/cirogomesoficial/)
3. Twitter
    - [Jair Bolsonaro](https://twitter.com/jairbolsonaro)
    - [Geraldo Alckmin](https://twitter.com/geraldoalckmin)
    - [Fernando Haddad](https://twitter.com/haddad_fernando)
    - [Marina Silva](https://twitter.com/marinasilva)
    - [Ciro Gomes](https://twitter.com/cirogomes)
4. YouTube
    - [Jair Bolsonaro](https://www.youtube.com/user/jbolsonaro/videos)
    - [Geraldo Alckmin](https://www.youtube.com/channel/UCNxCni0Iv9pr7i_pQZ6ijlg/videos)
    - [Fernando Haddad](???)
    - [Marina Silva](https://www.youtube.com/user/msilvaonline/videos)
    - [Ciro Gomes](https://www.youtube.com/channel/UCHFO37KCJlMNUXNK21MV8SQ/videos)
5. Twitter tredding
    - [DebateNaBand](https://twitter.com/hashtag/DebateNaBand)
    - [DebateRedeTv](https://twitter.com/hashtag/debateRedetv?src=tren) 

 #### Datasets
 
 1. [WordNetAffectBR](http://www.inf.pucrs.br/linatural/wordpress/index.php/recursos-e-ferramentas/wordnetaffectbr/)

 > Essa base foi construída para aplicações que utilizam vocabulário de palavras de emoções. Esse trabalho é relacionado ao estudo da análise de sentimentos em discurso da língua portuguesa.
 
 2. [SentiLex-PT01](http://xldb.fc.ul.pt/wiki/SentiLex-PT01)
 
 > SentiLex-PT01 é um léxico de sentimentos para o português constituído por 6.321 lemas adjectivais (por convenção, na forma masculina singular) e 25.406 formas flexionadas.

 3. [OpLexicon](http://ontolp.inf.pucrs.br/Recursos/downloads-OpLexicon.php)
 
 > OpLexicon é um léxico de sentimento para a língua portuguesa.

 4. [ViesNoticias](http://www.each.usp.br/norton/viesnoticias/index_ing.html) 

 > Este repositório conta com um corpus de notícias sobre política obtido de alguns produtores de notícias no Brasil.

 5. [Projeto Floresta Sintá(c)tica](https://www.linguateca.pt/Floresta/)
 
 > Chamamos de "Floresta Sintáctica" um conjunto de frases (corpus) analisadas (morfo)sintaticamente. Como, além da indicação das funções sintácticas, a análise também explicita hierarquicamente informação relativa à estrutura de constituintes, dizemos que uma frase sintaticamente analisada se parece com uma árvore, donde um conjunto de árvores constitui uma floresta sintáctica (em inglês, treebank).

 6. ***rever?*** [CETEMPúblico](https://www.linguateca.pt/acesso/corpus.php?corpus=CETEMPUBLICO)
 
 > O CETEMPúblico (Corpus de Extractos de Textos Electrónicos MCT/Público) é um corpus de aproximadamente 180 milhões de palavras em português europeu, criado pelo projecto Processamento computacional do português (projecto que deu origem à Linguateca) após a assinatura de um protocolo entre o Ministério da Ciência e da Tecnologia (MCT) português e o jornal PÚBLICO em Abril de 2000.

 #### Referências
 
 1. [TweetSentBR](https://bitbucket.org/HBrum/tweetsentbr/overview)
 
 > TweetSentBR is a corpus of Tweets in Brazilian Portuguese. It was labeled by several annotators following steps stablished on the literature for improving reliability on the task of Sentiment Analysis. Each Tweet was annotated in one of the three following classes: Positive - tweets where a user meant a positive reaction or evaluation about the main topic on the post; Negative - tweets where a user meant a negative reaction or evaluation about the main topic on the post; * Neutral - tweets not belonging to any of the last classes, usually not making a point, out of topic, irrelevant, confusing or containing only objective data.

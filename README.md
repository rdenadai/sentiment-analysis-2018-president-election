# Sentiment Analysis for 2018 Presidential Election

Análise de sentimentos relacionados aos candidatos a Eleição para a presidência de 2018.

### Descrição

Este é o projeto realizado para a conclusão da disciplina [IA369-Y Computação Afetiva](http://www.dca.fee.unicamp.br/~paula/teaching.html) realizada na Unicamp durante o 
2°Semestre 2018, oferecida pela Prof. Paula Dornhofer Paro Costa ([mais informações](http://www.dca.fee.unicamp.br/~paula/)).

Os integrantes do projeto são:
 - Edgar Lopes Banhesse
 - [Rodolfo De Nadai](http://www.rdenadai.com.br)

### Motivação

 - Nova forma de fazer campanha política, da TV e Rádio para Redes Sociais

 - Eleição presidencial dos Estados Unidos em 2016 foi marcada pelo uso das redes sociais como forma de se aproximar e entender os anseios do eleitorado americano

 - No Brasil em 2018, as redes sociais foram utilizadas na divulgação de propostas dos candidatos e na conquista do eleitorado brasileiro

 - Portanto, a análise de valências e emoções nos comentários nas redes sociais do Brasil (Instagram, Facebook, Twitter e Youtube), referentes a eleição presidencial Brasileira, pode contribuir para entender o papel das emoções no resultado da eleição e apresentar um panorama de influência entre o eleitorado (BERMINGHAM; SMEATON, 2011) (PÉREZ-ROSAS et al., 2017)


### Objetivo

Analisar as valências e emoções em comentários (textos) das principais redes sociais utilizadas no Brasil: Instagram, Facebook, Twitter (Tweets e Tendências) e Youtube referentes a eleição para presidente do Brasil em 2018.


### Abordagem Proposta

Utilizar modelo de emoção categórico baseado em valências e emoções com uma abordagem supervisionada composta por três etapas:

 - *Coleta dos comentários* - coletar comentários cinco candidatos melhor classificados nas pesquisas eleitorais para presidente (Jair Bolsonaro, Geraldo Alckmin, Fernando Haddad (Lula), Marina Silva e Ciro Gomes) nas redes sociais (Facebook, Instagram, Twitter e Youtube)

 - *Classificação dos comentários* - tratar os comentários e realizar testes para escolher o melhor classificador e os melhores datasets a serem utilizados para gerar as valências e emoções para os comentários coletados

 - *Análise dos resultados* - analisar os resultados obtidos, após a classificação dos comentários para tentar entender o papel das emoções no resultado da eleição para presidente no Brasil e apresentar um panorama de influência entre o eleitorado


### Histórico do Desenvolvimento

Inicialmente para analisar as valências e as emoções nos comentários foi decidido  fazer uma busca na internet por datasets com frases em português do 
Brasil rotuladas com valências e emoções.

Alguns datasets com rótulos de valências foram encontrados no site Minerando Dados, são eles:
 
 - Títulos de notícias, aproximadamente 2.000 linhas.
 
 - Tweets de Minas Gerais, aproximadamente 3.000 linhas.

Nessa busca inicial nenhum dataset rotulado com emoções foi encontrado. Dessa forma, optou-se a utilizar um método não 
supervisionado de identificação de emoções em textos curtos para o português proposto pela mestranda [Barbara Martinazzo](https://www.ppgia.pucpr.br/pt/arquivos/mestrado/dissertacoes/2010/barbara_martinazzo_versaofinal.pdf).
Foi aplicado o procedimento descrito para validação e análise de sentimentos em mensagens coletadas pela internet e em uma base de tweets coletados, 
os quais foram amostrados e definidos sentimentos prévios no trabalho do mestrando [Henrico Brum](https://bitbucket.org/HBrum/tweetsentbr/overview).

Os resultados preliminares do proposto acima podem ser observado neste [jupyter notebook](https://github.com/rdenadai/sentiment-analysis-2018-president-election/blob/master/src/ai/validate.ipynb). 

O trabalho realizado pela Barbara Martinazzo, for expandido, levando em consideração também uma emoção de neutralidade, algo que é mencionado em seu trabalho, mas não fora abordado.

Além disso, o algoritmo implementado, não aborda a questão discutida por ela, com relação a usar essa implementação para novas mensagens.
A abordagem utilizada por ela, leva em consideração o uso de contagem de palavras apenas (termo-documento), mas no algoritmo é possível optar pelo uso do 
[TF-IDF](https://pt.wikipedia.org/wiki/Tf%E2%80%93idf) para o cálculo das emoções.

Entretanto após a implementação do método proposto por Martinazzo, os resultados ficaram aquém do esperado, com taxa de identificação na faixa dos 30%.
Em contato com o grupo de pesquisa da Pontifícia Universidade Católica do Paraná no site Emoções foi obtido um dataset rotulado com as seis emoções de Ekman:
 
 - Títulos de notícias, aproximadamente 1.000 linhas.

Mesmo tendo em mãos essa base, os resultados ficaram aquém do esperado. Neste sentido, crer-se que em alguma parte o algoritmo não fora implementado corretamente.

Procurou-se aplicar uma nova abordagem baseada na clusterização de textos (Topic Modeling).
Existem diversas abordagens para a clusterização, como descrito por (MOODY, 2015) e (YUAN; HUANG; WU, 2016).
Para validar a possibilidade de identificação de emoções usando o conceito de modelagem por tópicos, utilizou-se o algoritmo t-SNE (*t-Distributed Stochastic Neighbor Embedding*) (MAATEN; HINTON, 2007),
o qual permite redução de dimensionalidade e agrupamento das estruturas por tópicos dentro do espaço vetorial.

Apesar dos resultados preliminares terem sido medianos e promissores, com uma acurácia em torno de 65%, 
o método é demasiadamente “caótico” devido a natureza do algoritmo. Neste sentido, seria necessário um estudo melhor e 
mais profundo das implicações necessárias a sua utilização.

Entretanto com essa base de dados, e outros datasets (ver seção datasets abaixo), optou-se por experimentar a utilização de métodos de aprendizado supervisionado.

Os resultados no reconhecimento de emoções (As 6 emoções de Eckman), podem ser observadas neste [jupyter notebook](https://github.com/rdenadai/sentiment-analysis-2018-president-election/blob/master/src/ai/experiments/supervised/regular_supervised_ml.ipynb)
 o qual acarretou em resultados na faixa dos 54%.

Outra tentativa de treinamento supervisionado pode ser observado neste outro [jupyter notebook](https://github.com/rdenadai/sentiment-analysis-2018-president-election/blob/wip_rdenadai/src/ai/experiments/supervised/valence_regular_supervised_ml.ipynb),
neste caso busca-se a valência de positivo/negativo/neutro, utilizando-se de várias técnicas chega-se a uma acurácia de aproximadamente 57%.

O presente projeto, apresenta todo o código do desenvolvimento descrito acima, além de todo o conteúdo de apoio ao desenvolvimento da aplicação final proposta.

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
    $> python -m nltk.downloader stopwords
    $> python -m nltk.downloader punkt
    $> python -m nltk.downloader rslp
    $> python -m nltk.downloader perluniprops
    $> python -m spacy download en
    $> python -m spacy download pt
    $> python cython_setup.py build_ext --inplace
    ```
 3.
    ```bash
    DATABASE_PATH=/home/root/sentiment_analysis.db
    FACEBOOK_USER=
    FACEBOOK_PASSWORD=
    ```
 4. Extraia e copie o conteúdo da pasta **selenium_driver** caso queira executar o passo 4.
 5. Execute o arquivo extractor.py caso queira extrair novamente os dados das redes sociais.
    ```bash
    $> python scraping/extractor.py
    $> python sanitization/clean.py
    ```

#### Páginas extraídas

Para a validação final sobre o sentimentos dos eleitores com relação aos candidatos a eleição do Brasil para 2018, 
foi realizado a raspagem de comentários das seguintes páginas de redes sociais. 

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
5. Twitter treding hashtags
    - [eleicoes2018](https://twitter.com/hashtag/eleicoes2018)
    - [eleições2018](https://twitter.com/hashtag/eleições2018)
    - [Eleições2018](https://twitter.com/hashtag/Eleições2018)
    - [eleicao2018](https://twitter.com/hashtag/eleicao2018)
    - [Eleição2018](https://twitter.com/hashtag/Eleição2018)
    - [DebateNaBand](https://twitter.com/hashtag/DebateNaBand)
    - [DebateRedeTv](https://twitter.com/hashtag/debateRedetv)
    - [GNEleicoes2018](https://twitter.com/hashtag/GNEleicoes2018)
    - [CiroNoJornalNacional](https://twitter.com/hashtag/CiroNoJornalNacional)
    - [CiroNaGloboNews](https://twitter.com/hashtag/CiroNaGloboNews)
    - [gneleicoes2018](https://twitter.com/hashtag/gneleicoes2018)
    - [BolsonaroNoJornalNacional](https://twitter.com/hashtag/BolsonaroNoJornalNacional)
    - [bolsonaronaglobonews](https://twitter.com/hashtag/bolsonaronaglobonews)
    - [GeraldoNoJN](https://twitter.com/hashtag/GeraldoNoJN)
    - [AlckminNoJornalNacional](https://twitter.com/hashtag/AlckminNoJornalNacional)
    - [GERALDONAGLOBONEWS](https://twitter.com/hashtag/GERALDONAGLOBONEWS)
    - [MarinaNoJornalNacional](https://twitter.com/hashtag/MarinaNoJornalNacional)
    - [Marinanaglobonews](https://twitter.com/hashtag/Marinanaglobonews)
    - [HaddadPresidente](https://twitter.com/hashtag/HaddadPresidente)
    - [HaddadÉLulaNoJN](https://twitter.com/hashtag/HaddadÉLulaNoJN)
    - [QuemMandouMatarBolsonaro](https://twitter.com/hashtag/QuemMandouMatarBolsonaro)
    - [Bolsonaro17](https://twitter.com/hashtag/Bolsonaro17)
    - [Geraldo45](https://twitter.com/hashtag/Geraldo45)
    - [Marina18](https://twitter.com/hashtag/Marina18)
    - [Haddad13](https://twitter.com/hashtag/Haddad13)
    - [Ciro12](https://twitter.com/hashtag/Ciro12)
    - [CiroGomes](https://twitter.com/hashtag/CiroGomes)
    - [GeraldoAlckmin](https://twitter.com/hashtag/GeraldoAlckmin)
    - [MarinaSilvaeEduardoJorge18](https://twitter.com/hashtag/MarinaSilvaeEduardoJorge18)
    - [HaddadELula](https://twitter.com/hashtag/HaddadELula)
    - [JairBolsonaro17](https://twitter.com/hashtag/JairBolsonaro17)
    - [EleSim](https://twitter.com/hashtag/EleSim)
    - [EleNão](https://twitter.com/hashtag/EleNão)
    - [BolsonaroNaJovemPan](https://twitter.com/hashtag/BolsonaroNaJovemPan)
    - [AlckminELula](https://twitter.com/hashtag/AlckminELula)
    - [Vote13](https://twitter.com/hashtag/Vote13)
    - [RuanetNÃO](https://twitter.com/hashtag/RuanetNÃO)
    - [DebateSBT](https://twitter.com/hashtag/DebateSBT)
    - [bolsonaroladrão](https://twitter.com/hashtag/bolsonaroladrão)
    - [bolsonaronacadeia](https://twitter.com/hashtag/bolsonaronacadeia)
    - [veja600milhoes](https://twitter.com/hashtag/veja600milhoes)
    - [elesimeno1turno](https://twitter.com/hashtag/elesimeno1turno)
    - [ÉPelaVidadasMulheres](https://twitter.com/hashtag/ÉPelaVidadasMulheres)
    - [mudabrasilcombolsonaro](https://twitter.com/hashtag/mudabrasilcombolsonaro)
    - [OVotoNaRecord](https://twitter.com/hashtag/OVotoNaRecord)
    - [OVotoNaRecordNews](https://twitter.com/hashtag/OVotoNaRecordNews)
    - [DebateNaRecord](https://twitter.com/hashtag/DebateNaRecord)
    - [DebateNaGlobo](https://twitter.com/hashtag/DebateNaGlobo)
    - [ViraViraCiro](https://twitter.com/hashtag/ViraViraCiro)
    - [BolsonaroNaRecord](https://twitter.com/hashtag/BolsonaroNaRecord)
    - [Dia7é17](https://twitter.com/hashtag/Dia7é17)
    - [EuVotoBolsonaro](https://twitter.com/hashtag/EuVotoBolsonaro)
    - [ManuNoJaburu](https://twitter.com/hashtag/ManuNoJaburu)
    - [Haddadé13](https://twitter.com/hashtag/haddadé13)
    - [GeraldoPresidente](https://twitter.com/hashtag/geraldopresidente)
    - [17Neles](https://twitter.com/hashtag/17Neles)
    - [FraudeNasUrnasEletronicas](https://twitter.com/hashtag/FraudeNasUrnasEletronicas)
    - [FicaTemer](https://twitter.com/hashtag/FicaTemer)
    - [AgoraÉHaddad](https://twitter.com/hashtag/AgoraÉHaddad)
    - [Nordeste17](https://twitter.com/hashtag/Nordeste17)
    - [HaddadSim](https://twitter.com/hashtag/HaddadSim)
    - [VemProDebate](https://twitter.com/hashtag/VemProDebate)
    - [BolsonaroCagao](https://twitter.com/hashtag/BolsonaroCagao)
    - [LulaTaPresoBabaca](https://twitter.com/hashtag/LulaTaPresoBabaca)
    - [DitaduraNuncaMais](https://twitter.com/hashtag/DitaduraNuncaMais)
    - [Caixa2doBolsonaro](https://twitter.com/hashtag/Caixa2doBolsonaro)
    - [MarketeirosDoJair](https://twitter.com/hashtag/MarketeirosDoJair)
    - [Bolsolao](https://twitter.com/hashtag/Bolsolao)
    - [AtentadoFakeDoPT](https://twitter.com/hashtag/AtentadoFakeDoPT)
    - [HaddadNaoECristao](https://twitter.com/hashtag/HaddadNaoECristao)
    - [SuasticaFake](https://twitter.com/hashtag/SuasticaFake)
    - [BolsonaroPredsidente](https://twitter.com/hashtag/BolsonaroPredsidente)
    - [FakeNewsDoHaddad](https://twitter.com/hashtag/FakeNewsDoHaddad)
    - [brasilcombolsonaro17](https://twitter.com/hashtag/brasilcombolsonaro17)
    - [CagueiproIbope](https://twitter.com/hashtag/CagueiproIbope)
    - [NãoAceitaremosFraudes](https://twitter.com/hashtag/NãoAceitaremosFraudes)
    - [BolsonaroPresidenteEleito](https://twitter.com/hashtag/BolsonaroPresidenteEleito)
    - [OBrasilFelizDeNovo](https://twitter.com/hashtag/OBrasilFelizDeNovo)
    - [BrasilViraHaddad](https://twitter.com/hashtag/BrasilViraHaddad)
    - [AndradeJaEra](https://twitter.com/hashtag/AndradeJaEra)
    - [ViraVotoHaddad13](https://twitter.com/hashtag/ViraVotoHaddad13)
    - [AcabouaPiranhagemPT](https://twitter.com/hashtag/AcabouaPiranhagemPT)
    - [OBrasilVota17](https://twitter.com/hashtag/OBrasilVota17)
    - [ViraVirouHaddad](https://twitter.com/hashtag/ViraVirouHaddad)
    - [HadadPresidente13](https://twitter.com/hashtag/HadadPresidente13)
    - [APesardoPToBrasilVaiVencerB17](https://twitter.com/hashtag/APesardoPToBrasilVaiVencerB17)
    - [PrayForBrazil](https://twitter.com/hashtag/PrayForBrazil)
    - [RIPBrasil](https://twitter.com/hashtag/RIPBrasil)
    - [EleNaoEMeuPresidente](https://twitter.com/hashtag/EleNaoEMeuPresidente)
    - [meubolsominionsecreto](https://twitter.com/hashtag/meubolsominionsecreto)
 
 #### Léxicos
 
 Coletamos e analisamos o uso dos seguintes possíveis léxicos para a língua portuguesa.
 
 No momento presente o trabalho se baseia na união do [SentiLex + OpLexicon + Conjuntos de palavras por sentimentos](https://github.com/rdenadai/sentiment-analysis-2018-president-election/tree/master/dataset/emocoes).
 
1 . [WordNetAffectBR](http://www.inf.pucrs.br/linatural/wordpress/index.php/recursos-e-ferramentas/wordnetaffectbr/)

 > Essa base foi construída para aplicações que utilizam vocabulário de palavras de emoções. Esse trabalho é relacionado ao estudo da análise de sentimentos em discurso da língua portuguesa.
 
2 . [SentiLex-PT](https://b2share.eudat.eu/records/93ab120efdaa4662baec6adee8e7585f)
 
 > SentiLex-PT01 é um léxico de sentimentos para o português constituído por 6.321 lemas adjectivais (por convenção, na forma masculina singular) e 25.406 formas flexionadas.
 
 > SentiLex-PT02 is a sentiment lexicon for Portuguese, made up of 7,014 lemmas, and 82,347 inflected forms. In detail, the lexicon describes: 4,779 (16,863) adjectives, 1,081 (1,280) nouns, 489 (29,504) verbs, and 666 (34,700) idiomatic expressions. The sentiment entries correspond to human predicates, i.e. predicates modifying human nouns, compiled from different publicly available resources (corpora and dictionaries). SentiLex-PT is especially useful for opinion mining applications involving Portuguese, in particular for detecting and classifying sentiments and opinions targeting human entities. 

  - [SentiLex-PT01](http://xldb.fc.ul.pt/wiki/SentiLex-PT01)
  - [SentiLex-PT02](https://b2share.eudat.eu/records/93ab120efdaa4662baec6adee8e7585f)

3 . [OpLexicon v2.1 & v3.0](http://ontolp.inf.pucrs.br/Recursos/downloads-OpLexicon.php)
 
 > OpLexicon é um léxico de sentimento para a língua portuguesa.

 ### Datasets

1 . [TweetSentBR](https://bitbucket.org/HBrum/tweetsentbr/overview)

 > TweetSentBR is a corpus of Tweets in Brazilian Portuguese. It was labeled by several annotators following steps stablished on the literature for improving reliability on the task of Sentiment Analysis. Each Tweet was annotated in one of the three following classes: Positive - tweets where a user meant a positive reaction or evaluation about the main topic on the post; Negative - tweets where a user meant a negative reaction or evaluation about the main topic on the post; * Neutral - tweets not belonging to any of the last classes, usually not making a point, out of topic, irrelevant, confusing or containing only objective data.

2 . [EMOÇÕES.BR](http://www.ppgia.pucpr.br/~paraiso/mineracaodeemocoes/index.php)
 
 > Projeto desenvolvido no Programa de Pós-Graduação em Informática da Pontifícia Universidade Católica do Paraná

3 . [MinerandoDados](https://github.com/minerandodados/mdrepo/blob/master/Tweets_Mg.csv)
 
 > Repositório para armazenamento de código e notebooks de postagens do blog e cursos.

4 . [ViesNoticias](http://www.each.usp.br/norton/viesnoticias/index_ing.html) 

 > Este repositório conta com um corpus de notícias sobre política obtido de alguns produtores de notícias no Brasil.

5 . [Projeto Floresta Sintá(c)tica](https://www.linguateca.pt/Floresta/)
 
 > Chamamos de "Floresta Sintáctica" um conjunto de frases (corpus) analisadas (morfo)sintaticamente. Como, além da indicação das funções sintácticas, a análise também explicita hierarquicamente informação relativa à estrutura de constituintes, dizemos que uma frase sintaticamente analisada se parece com uma árvore, donde um conjunto de árvores constitui uma floresta sintáctica (em inglês, treebank).

 
 ##### Python libs

1 . Para realizar toda a operação estamos utilizando as seguintes bibliotecas:

 - [selenium](https://selenium-python.readthedocs.io/)
    > Utlizada para realizar a raspagem dos comentários e outros dados das páginas apresentadas abaixo.
      Infelizmente as api's das redes sociais são bem mais restritivas agora, ou mesmo tem um tempo moroso para habilitação de uso.
 - [peewee](http://docs.peewee-orm.com/en/latest/)
    > ORM em python para realizar a conexão com a base de dados. No caso estamos utilizando sqlite como base de dados.
 - [NLTK](http://www.nltk.org/howto/portuguese_en.html)
    > Natural Language Toolkit em python, foi utilizada em alguns pontos específicos para realizar o tratamento e análise de textos. 
 - [spaCy](https://spacy.io/usage/spacy-101)
    > É uma exceleten biblioteca para NLP, adiciona várioas algoritmos e ferramental para análise de textos.
 - [gensim](https://radimrehurek.com/gensim/)
    > Topic Modelling for Humans
 - [scikit-learn](http://scikit-learn.org)
    > Excelente ferramenta para Machine Learning, mas possui diversas funções matemáticas prontas. Usamos suas operações para trabalhar com texto.
 - [Cython](https://cython.org/)
    > Converte código python para C, permitindo melhorias na performance de execução.
 - [numba](http://numba.pydata.org/)
    > Compilador JIT que converte código python para C, permitindo melhorias na performance de execução.
 - [numpy](http://www.numpy.org/)
 - [scipy](https://www.scipy.org/)
 - [matplotlib](https://matplotlib.org/)
 - [pandas](https://pandas.pydata.org/)
    > Ferramentas padrão e essenciais para projetos de data science e machine learning.
 
 
 ### Extras
 
1 . Dados Extras:
  - [Frases para Face](https://www.frasesparaface.com.br/outras-frases/)
  - [Dicionário Criativo](https://dicionariocriativo.com.br/)
 
2 . Tutoriais
  - [Utilizando processamento de linguagem natural para criar uma sumarização automática de textos](https://medium.com/@viniljf/utilizando-processamento-de-linguagem-natural-para-criar-um-sumariza%C3%A7%C3%A3o-autom%C3%A1tica-de-textos-775cb428c84e)
  - [Latent Semantic Analysis (LSA) for Text Classification Tutorial](http://mccormickml.com/2016/03/25/lsa-for-text-classification-tutorial/)
  - [Machine Learning :: Cosine Similarity for Vector Space Models (Part III)](http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/)
  - [My Notes for Singular Value Decomposition with Interactive Code ](https://towardsdatascience.com/my-notes-for-singular-value-decomposition-with-interactive-code-feat-peter-mills-7584f4f2930a)
  - [Principal Component Analysis in Python](https://plot.ly/ipython-notebooks/principal-component-analysis/)
  - [Euclidean vs. Cosine Distance](https://cmry.github.io/notes/euclidean-v-cosine)
  - [Word embeddings: exploration, explanation, and exploitation](https://towardsdatascience.com/word-embeddings-exploration-explanation-and-exploitation-with-code-in-python-5dac99d5d795)
  - [Complete Guide to Word Embeddings](https://nlpforhackers.io/word-embeddings/)
  - [An Intuitive Understanding of Word Embeddings: From Count Vectors to Word2Vec](https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/)
  - [torchtext](https://spacy.io/universe/?id=tochtext)
 
3 . Topic Modelling
  - [Topic Modeling with LSA, PLSA, LDA & lda2Vec](https://medium.com/nanonets/topic-modeling-with-lsa-psla-lda-and-lda2vec-555ff65b0b05)
  - [Integrating Topics and Syntax (HHM-LDA)](http://psiexp.ss.uci.edu/research/papers/composite.pdf)
  - [Visualizing MNIST: An Exploration of Dimensionality Reduction](http://colah.github.io/posts/2014-10-Visualizing-MNIST/)
  - [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/)
  - [sense2vec](https://spacy.io/universe/?id=sense2vec)
 
4 . LSA + Others
  - [Um Método de Identificação de Emoções em Textos Curtos para o Português do Brasil](http://www.ppgia.pucpr.br/~paraiso/Projects/Emocoes/Emocoes.html)
  - [An Introduction to Latent Semantic Analysis](http://lsa.colorado.edu/papers/dp1.LSAintro.pdf)
  - [Unsupervised Emotion Detection from Text using Semantic and Syntactic Relations](http://www.cse.yorku.ca/~aan/research/paper/Emo_WI10.pdf)
  - [An Efficient Method for Document Categorization Based on Word2vec and Latent Semantic Analysis](https://ieeexplore.ieee.org/document/7363382)
  - [Sentiment Classification of Documents Based on Latent Semantic Analysis](https://link.springer.com/chapter/10.1007/978-3-642-21802-6_57)
  - [Applying latent semantic analysis to classify emotions in Thai text](https://ieeexplore.ieee.org/document/5486137)
  - [Text Emotion Classification Research Based on Improved Latent Semantic Analysis Algorithm](https://www.researchgate.net/publication/266651993_Text_Emotion_Classification_Research_Based_on_Improved_Latent_Semantic_Analysis_Algorithm)
  - [PANAS-t: A Pychometric Scale for Measuring Sentiments on Twitter](https://arxiv.org/abs/1308.1857)


### Referências

BERMINGHAM, A.; SMEATON, A. F. On using Twitter to monitor political sentiment and predict election results, 1 jan. 2011.

EKMAN, P.; FRIESEN, W. V. The facial action coding system. Palo Alto, CA: Consulting Psychologists Press, 1976.

JU, R. et al. An Efficient Method for Document Categorization Based on Word2vec and Latent Semantic Analysis, 1 jan. 2015.

LANDAUER, T. K.; FOLTZ, P. W.; LAHAM, D. An introduction to latent semantic analysis. Discourse Processes, v. 25, n. 2-3, p. 259-284, 1 jan. 1998.

MAATEN, L. VAN DER; HINTON, G. Visualizing Data using t-SNE. Journal of Machine Learning Research, v. 9, n. Nov, p. 2579-2605, 2007.

MARTINAZZO, B.; PARAISO, E. C. Um Método de Identificação de Emoções em Textos Curtos para o Português do Brasil. [s.l: s.n.].

MIKOLOV, T. et al. Distributed representations of words and phrases and their compositionality text mining. 2012.

MOODY, C. E. Mixing Dirichlet Topic Models and Word Embeddings to Make lda2vec. arXiv: 1605.02019, p. 8, 2015.

PÉREZ-ROSAS, V. et al. Automatic Detection of Fake News, 23 ago. 2017.

PICARD, R. . Affective Computing. 2nd. ed. Cambridge, MA: MIT Press, 1995.

PIYATIDA INRAK; SUKREE SINTHUPINYO. Applying latent semantic analysis to classify emotions in Thai text. 2010 2nd International Conference on Computer Engineering and Technology. Anais...IEEE, [s.d.]

STRAPPARAVA, C.; MIHALCEA, R. Learning to identify emotions in text. Proceedings of the 2008 ACM symposium on Applied computing - SAC ’08. Anais...ACM Press, 2006. Acesso em: 2006

WANG, X.; ZHENG, Q. Text Emotion Classification Research Based on Improved Latent Semantic Analysis Algorithm. Proceedings of the 2nd International Conference on Computer Science and Electronics Engineering (ICCSEE 2013). Anais...Atlantis Press, 2011. Acesso em: 2011

YUAN, S.; HUANG, H.; WU, L. Use of Word Clustering to Improve Emotion Recognition from Short Text. Journal of Computing Science and Engineering, v. 10, n. 4, 30 dez. 2016.
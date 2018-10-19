# Sentiment Analysis for 2018 Presidential Election

Análise de sentimentos relacionados aos candidatos a Eleição para a presidência de 2018.

### Objetivo

Este é o projeto realizado para a conclusão da disciplina [IA369-Y Computação Afetiva](http://www.dca.fee.unicamp.br/~paula/teaching.html) realizada na Unicamp durante o 
2°Semestre 2018, oferecidade pela Prof. Paula Dornhofer Paro Costa ([mais informações](http://www.dca.fee.unicamp.br/~paula/)).

O principal objetivo do projeto é coletar, analisar e detectar as emoções das pessoas com relação aos candidatos às eleições
a presidência no Brasil para o ano de 2018.

Os integrantes do projeto são:
 - Edgar Lopes Banhesse
 - [Rodolfo De Nadai](http://www.rdenadai.com.br)

### Descrição

Utilizando-se do algoritmo proposto pela mestranda [Barbara Martinazzo](https://www.ppgia.pucpr.br/pt/arquivos/mestrado/dissertacoes/2010/barbara_martinazzo_versaofinal.pdf), foi aplicado
o procedimento descrito para validação e análise de sentimentos em mensagens coletadas pela internet e em uma base de tweets coletados, os quais foram amostrados e definidos sentimentos prévios no trabalho
do mestrando [Henrico Brum](https://bitbucket.org/HBrum/tweetsentbr/overview).

Os resultados preliminares do proposto acima podem ser observado neste [jupyter notebook](https://github.com/rdenadai/sentiment-analysis-2018-president-election/blob/master/src/ai/validate.ipynb). 

Expandimos o trabalho realizado pela Barbara Martinazzo, levando em consideração também uma emoção de neutralidade, algo que é mencionado em seu trabalho, mas não fora abordado.

Além, disso, esse algoritmo implementado, não aborda a questão discutida por ela, com relação a usar essa implementação para novas mensagens. A abordagem utilizada por ela, leva em consideração o uso de contagem de palavras apenas,
mas no algoritmo é possível optar pelo uso do [TF-IDF](https://pt.wikipedia.org/wiki/Tf%E2%80%93idf) para o cálculo das emoções.

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
    $> python -m nltk.downloader floresta
    $> python -m nltk.downloader mac_morpho
    $> python -m nltk.downloader machado
    $> python -m nltk.downloader stopwords
    $> python -m nltk.downloader rslp
    $> python -m spacy download en
    $> python -m spacy download pt
    $> cd src/ai/unsupervised/
    $> python setup.py build_ext --inplace

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
    $> python extractor.py
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
 
 #### Léxicos
 
 Coletamos e analisamos o uso dos seguintes possíveis léxicos para a língua portuguesa.
 
 Por fim, o trabalho atual se baseia na união do [SentiLex + OpLexicon + Conjuntos de palavras por sentimentos](https://github.com/rdenadai/sentiment-analysis-2018-president-election/tree/master/dataset/emocoes).
 
 
 1. [WordNetAffectBR](http://www.inf.pucrs.br/linatural/wordpress/index.php/recursos-e-ferramentas/wordnetaffectbr/)

 > Essa base foi construída para aplicações que utilizam vocabulário de palavras de emoções. Esse trabalho é relacionado ao estudo da análise de sentimentos em discurso da língua portuguesa.
 
 2. [SentiLex-PT](https://b2share.eudat.eu/records/93ab120efdaa4662baec6adee8e7585f)
 
 > SentiLex-PT01 é um léxico de sentimentos para o português constituído por 6.321 lemas adjectivais (por convenção, na forma masculina singular) e 25.406 formas flexionadas.
 
 > SentiLex-PT02 is a sentiment lexicon for Portuguese, made up of 7,014 lemmas, and 82,347 inflected forms. In detail, the lexicon describes: 4,779 (16,863) adjectives, 1,081 (1,280) nouns, 489 (29,504) verbs, and 666 (34,700) idiomatic expressions. The sentiment entries correspond to human predicates, i.e. predicates modifying human nouns, compiled from different publicly available resources (corpora and dictionaries). SentiLex-PT is especially useful for opinion mining applications involving Portuguese, in particular for detecting and classifying sentiments and opinions targeting human entities. 

  - [SentiLex-PT01](http://xldb.fc.ul.pt/wiki/SentiLex-PT01)
  - [SentiLex-PT02](https://b2share.eudat.eu/records/93ab120efdaa4662baec6adee8e7585f)

 3. [OpLexicon v2.1 & v3.0](http://ontolp.inf.pucrs.br/Recursos/downloads-OpLexicon.php)
 
 > OpLexicon é um léxico de sentimento para a língua portuguesa.

 ### Datasets

 1. [ViesNoticias](http://www.each.usp.br/norton/viesnoticias/index_ing.html) 

 > Este repositório conta com um corpus de notícias sobre política obtido de alguns produtores de notícias no Brasil.

 2. [Projeto Floresta Sintá(c)tica](https://www.linguateca.pt/Floresta/)
 
 > Chamamos de "Floresta Sintáctica" um conjunto de frases (corpus) analisadas (morfo)sintaticamente. Como, além da indicação das funções sintácticas, a análise também explicita hierarquicamente informação relativa à estrutura de constituintes, dizemos que uma frase sintaticamente analisada se parece com uma árvore, donde um conjunto de árvores constitui uma floresta sintáctica (em inglês, treebank).

 #### Referências
 
 1 . [TweetSentBR](https://bitbucket.org/HBrum/tweetsentbr/overview)
 
 > TweetSentBR is a corpus of Tweets in Brazilian Portuguese. It was labeled by several annotators following steps stablished on the literature for improving reliability on the task of Sentiment Analysis. Each Tweet was annotated in one of the three following classes: Positive - tweets where a user meant a positive reaction or evaluation about the main topic on the post; Negative - tweets where a user meant a negative reaction or evaluation about the main topic on the post; * Neutral - tweets not belonging to any of the last classes, usually not making a point, out of topic, irrelevant, confusing or containing only objective data.
 
 ##### Python libs

 Para realizar toda a operação estamos utilizando as seguintes bibliotecas:

 - [selenium](https://selenium-python.readthedocs.io/)
    > Utlizada para realizar a raspagem dos comentários e outros dados das páginas apresentadas abaixo.
      Infelizmente as api's das redes sociais são bem mais restritivas agora, ou mesmo tem um tempo moroso para habilitação de uso.
 - [peewee](http://docs.peewee-orm.com/en/latest/)
    > ORM em python para realizar a conexão com a base de dados. No caso estamos utilizando sqlite como base de dados.
 - [NLTK](http://www.nltk.org/howto/portuguese_en.html)
    > Natural Language Toolkit em python, foi utilizada em alguns pontos específicos para realizar o tratamento e análise de textos. 
 - [spaCy](https://spacy.io/usage/spacy-101)
    > É uma exceleten biblioteca para NLP, adiciona várioas algoritmos e ferramental para análise de textos.
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
 
 
 3 . Dados:
  - [Frases para Face](https://www.frasesparaface.com.br/outras-frases/)
  - [Dicionário Criativo](https://dicionariocriativo.com.br/)
  
 
 4 . Tutoriais
  - [Utilizando processamento de linguagem natural para criar uma sumarização automática de textos](https://medium.com/@viniljf/utilizando-processamento-de-linguagem-natural-para-criar-um-sumariza%C3%A7%C3%A3o-autom%C3%A1tica-de-textos-775cb428c84e)
  - [Latent Semantic Analysis (LSA) for Text Classification Tutorial](http://mccormickml.com/2016/03/25/lsa-for-text-classification-tutorial/)
  - [Machine Learning :: Cosine Similarity for Vector Space Models (Part III)](http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/)
  - [My Notes for Singular Value Decomposition with Interactive Code ](https://towardsdatascience.com/my-notes-for-singular-value-decomposition-with-interactive-code-feat-peter-mills-7584f4f2930a)
  - [Principal Component Analysis in Python](https://plot.ly/ipython-notebooks/principal-component-analysis/)
  - [Euclidean vs. Cosine Distance](https://cmry.github.io/notes/euclidean-v-cosine)
 
 5 . Topic Modelling
  - [Topic Modeling with LSA, PLSA, LDA & lda2Vec](https://medium.com/nanonets/topic-modeling-with-lsa-psla-lda-and-lda2vec-555ff65b0b05)
  - [Integrating Topics and Syntax (HHM-LDA)](http://psiexp.ss.uci.edu/research/papers/composite.pdf)
 
 6 . LSA + Others
  - [Um Método de Identificação de Emoções em Textos Curtos para o Português do Brasil](http://www.ppgia.pucpr.br/~paraiso/Projects/Emocoes/Emocoes.html)
  - [An Introduction to Latent Semantic Analysis](http://lsa.colorado.edu/papers/dp1.LSAintro.pdf)
  - [Unsupervised Emotion Detection from Text using Semantic and Syntactic Relations](http://www.cse.yorku.ca/~aan/research/paper/Emo_WI10.pdf)
  - [An Efficient Method for Document Categorization Based on Word2vec and Latent Semantic Analysis](https://ieeexplore.ieee.org/document/7363382)
  - [Sentiment Classification of Documents Based on Latent Semantic Analysis](https://link.springer.com/chapter/10.1007/978-3-642-21802-6_57)
  - [Applying latent semantic analysis to classify emotions in Thai text](https://ieeexplore.ieee.org/document/5486137)
  - [Text Emotion Classification Research Based on Improved Latent Semantic Analysis Algorithm](https://www.researchgate.net/publication/266651993_Text_Emotion_Classification_Research_Based_on_Improved_Latent_Semantic_Analysis_Algorithm)
  - [PANAS-t: A Pychometric Scale for Measuring Sentiments on Twitter](https://arxiv.org/abs/1308.1857)


# Sentiment Analysis for 2018 Presidential Election

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
    DATABASE_PATH=/home/root/sentiment_analysis.db
    FACEBOOK_USER=
    FACEBOOK_PASSWORD=
    ```
 4. Extraia e copie o conteúdo da pasta **selenium_driver** caso queira executar o passo 4.
 5. Execute o arquivo extractor.py caso queira extrair novamente os dados das redes sociais.
    ```bash
    $> python extractor.py
    ```

#### Python libs

Para realizar toda a operação estamos utilizando as seguintes bibliotecas:

 - selenium
    > Utlizada para realizar a raspagem dos comentários e outros dados das páginas apresentadas abaixo.
      Infelizmente as api's das redes sociais são bem mais restritivas agora, ou mesmo tem um tempo moroso para habilitação de uso.
 - peewee
    > ORM em python para realizar a conexão com a base de dados. No caso estamos utilizando sqlite como base de dados.
 
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
5. Twitter treding
    - [eleicoes2018](https://twitter.com/hashtag/eleicoes2018)
    - [eleições2018](https://twitter.com/hashtag/eleições2018)
    - [Eleições2018](https://twitter.com/hashtag/Eleições2018)
    - [eleicao2018](https://twitter.com/hashtag/eleicao2018)
    - [Eleição2018](https://twitter.com/hashtag/Eleição2018)
    - [DebateNaBand](https://twitter.com/hashtag/DebateNaBand)
    - [DebateRedeTv](https://twitter.com/hashtag/debateRedetv)
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

 #### Datasets
 
 1. [WordNetAffectBR](http://www.inf.pucrs.br/linatural/wordpress/index.php/recursos-e-ferramentas/wordnetaffectbr/)

 > Essa base foi construída para aplicações que utilizam vocabulário de palavras de emoções. Esse trabalho é relacionado ao estudo da análise de sentimentos em discurso da língua portuguesa.
 
 2. [SentiLex-PT](https://b2share.eudat.eu/records/93ab120efdaa4662baec6adee8e7585f)
 
 > SentiLex-PT01 é um léxico de sentimentos para o português constituído por 6.321 lemas adjectivais (por convenção, na forma masculina singular) e 25.406 formas flexionadas.
 
 > SentiLex-PT02 is a sentiment lexicon for Portuguese, made up of 7,014 lemmas, and 82,347 inflected forms. In detail, the lexicon describes: 4,779 (16,863) adjectives, 1,081 (1,280) nouns, 489 (29,504) verbs, and 666 (34,700) idiomatic expressions. The sentiment entries correspond to human predicates, i.e. predicates modifying human nouns, compiled from different publicly available resources (corpora and dictionaries). SentiLex-PT is especially useful for opinion mining applications involving Portuguese, in particular for detecting and classifying sentiments and opinions targeting human entities. 

  - [SentiLex-PT01](http://xldb.fc.ul.pt/wiki/SentiLex-PT01)
  - [SentiLex-PT02](https://b2share.eudat.eu/records/93ab120efdaa4662baec6adee8e7585f)

 3. [OpLexicon v2.1 & v3.0](http://ontolp.inf.pucrs.br/Recursos/downloads-OpLexicon.php)
 
 > OpLexicon é um léxico de sentimento para a língua portuguesa.

 4. [ViesNoticias](http://www.each.usp.br/norton/viesnoticias/index_ing.html) 

 > Este repositório conta com um corpus de notícias sobre política obtido de alguns produtores de notícias no Brasil.

 5. [Projeto Floresta Sintá(c)tica](https://www.linguateca.pt/Floresta/)
 
 > Chamamos de "Floresta Sintáctica" um conjunto de frases (corpus) analisadas (morfo)sintaticamente. Como, além da indicação das funções sintácticas, a análise também explicita hierarquicamente informação relativa à estrutura de constituintes, dizemos que uma frase sintaticamente analisada se parece com uma árvore, donde um conjunto de árvores constitui uma floresta sintáctica (em inglês, treebank).

 #### Referências
 
 1. [TweetSentBR](https://bitbucket.org/HBrum/tweetsentbr/overview)
 
 > TweetSentBR is a corpus of Tweets in Brazilian Portuguese. It was labeled by several annotators following steps stablished on the literature for improving reliability on the task of Sentiment Analysis. Each Tweet was annotated in one of the three following classes: Positive - tweets where a user meant a positive reaction or evaluation about the main topic on the post; Negative - tweets where a user meant a negative reaction or evaluation about the main topic on the post; * Neutral - tweets not belonging to any of the last classes, usually not making a point, out of topic, irrelevant, confusing or containing only objective data.

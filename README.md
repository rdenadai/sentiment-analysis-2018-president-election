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
 3. Extraia e copie o conteúdo da pasta **selenium_driver** caso queira executar o passo 4.
 4. Execute o arquivo extractor.py caso queira extrair novamente os dados das redes sociais.
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

 #### Referências
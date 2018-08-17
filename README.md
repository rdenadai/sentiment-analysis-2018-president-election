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
 3. Crie um arquivo no diretório raiz com o nome .env, o qual deve conter
    ```bash
    TWITTER_CONSUMER_API=
    TWITTER_CONSUMER_SECRET=
    TWITTER_ACCESS_TOKEN=
    TWITTER_ACCESS_TOKEN_SECRET=
    ```
 4. Após isso estará pronto para iniciar o projeto.
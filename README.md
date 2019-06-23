# drf_api_framework
Baseado na Tech Talks do curso Python Pro, sobre Django Rest Framework - Parte 3

Está terceira parte foi feita utilizando o Framework Django REST framework.

Sugestão para que quiser fazer tudo na mão, 
e acompanhando a gravação da Tech Talk, como eu fiz, 
faça isso vendo todas as três Techs.

[Tech Talk Python Pro Part1](https://www.youtube.com/watch?v=Kt4AOh9jz-8&list=PLA05yVJtRWYSQ0loqX4Er6wIwJ_sU8j3S)

[Tech Talk Python Pro Part2](https://www.youtube.com/watch?v=TP5lI1Cuo2g)

Acesse a [Tech Talk Python Pro Part3](https://www.youtube.com/watch?v=ZB9D0kEMkqs), feita por
Riverfount e Renzo.

## Como desenvolver?

1. Clone o repositorio.
2. Crie um vertualenv com Python 3.7.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env

Acesso o link para ter melhor detalhamento do da instalção e implementação [Riverfount Part03](https://github.com/Riverfount/drf_api_presentation/blob/master/part03/PITCHME.md)

```console
https://github.com/gelhen/drf_api_framework.git drf_api_3
cd drf_api_3
python -m venv .venv 
source .venv\Scripts\activage
pip install -r requirements-dev.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

Faça o teste http://127.0.0.1:8000/drf/v1/tasks/

<h1 align="center"> Python Games </h1>

<p align="center">
  <img src="https://user-images.githubusercontent.com/81915403/196280980-c8c49731-8c7f-42fd-a246-d087c4927fbd.png" alt="Banner Python Games" height=400>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge" alt="Badge em Desenvolvimento">
</p>

Este projeto começou como resultado dos cursos de iniciação a Python na <a href=https://www.alura.com.br/>Alura</a>. Neles foram feitos dois jogos simples em Python: Adivinhe um número e Forca, para serem rodados no terminal, bem como um hub para que o usuário possa escolher o que quer jogar.

## ✔️ Técnicas e tecnologias utilizadas

- ``Python 3``
- ``Docker``

## Executando

A fim de garantir que o projeto rode em qualquer máquina, é necessário que se tenha o <a href="https://www.docker.com/get-started/">Docker</a> instalado.

Assim, para subir e executar um container da aplicação:
```
  docker image build -t python-games . && docker run -it python-games
```

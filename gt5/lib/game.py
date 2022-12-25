"""
Cria, remove, adciona e gere jogos na biblioteca
"""

import os
from os import system

if __name__ == "__main__":
    import utils
else:
    from lib import utils

CONFIG = ".config/game.config"
PASTA = "games"
BANNERPASTA = "banner"
id = 0


def save_id():
    """
    Guarda o id no ficheiro de configuração de jogos
    """
    global id, CONFIG

    utils.save(CONFIG, {"id": id})


def increment_id():
    """
    Incrementa o id e o salva
    """
    
    global id

    print(id)

    id += 1
    save_id()


def get_id() -> int:
    """
    Retorna o proximo id e o guarda na variavel a ser usado salvo na PASTA
    caso exita ou então cria um apartir de 1 e o salva
    """
    global id, CONFIG

    __data = utils.parser(CONFIG)

    if "id" in __data:
        print(__data)
        id = int(__data["id"])
    else:
        id = 1
        save_id()
    
    return id


id = get_id()


def criar_jogo(__data:dict) -> bool:
    """
    Cria um jogo e automaticamente adciona a biblioteca do usuario.

    __data: um dicionario contendo os dados do jogo

    __data.nome: nome do jogo (str)
    __data.username: o usuario que criou o jogo (str)
    __data.categoria: a categoria do jogo (str)
    __data.data: a data de lançamento do jogo (str)
    __data.tags: as tags do jogo (set)
    __data.privado: true se o jogo for privado (bool)
    """
    global id, PASTA

    utils.write(f'{PASTA}/{id}', __data)

    increment_id()


criar_jogo({"nome": "Undertale", "username": "filintodelgado",
            "categoria": "chorar", "data": "irrelevante", 
            "tags": ("test1", "test2"),
            "privado": False
           })

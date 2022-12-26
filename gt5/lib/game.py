"""
Cria, remove, adciona e gere jogos na biblioteca
"""

import os

if __name__ == "__main__":
    import utils
    import user
else:
    from lib import utils
    from lib import user

CONFIG = ".config/game.config"
PASTA = "games"
BANNERPASTA = "banner"
id = 0


def save_id():
    """
    Guarda o id no ficheiro de configuração de jogos
    """
    global id, CONFIG

    utils.write(CONFIG, {"id": id})


def increment_id():
    """
    Incrementa o id e o salva
    """
    
    global id

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
        id = int(__data["id"])
    else:
        id = 1
        save_id()
    
    return id


id = get_id()


def add_to_collection(__data:str, id):
    """
    Adciona a coleção do usuario
    """
    USERPATH = user.PASTA+"/"+__data["username"]

    userdata = utils.parser(USERPATH)

    try:
        userdata["games"].append(id)
    except KeyError:
        userdata["games"] = [id]
    
    utils.write(USERPATH, userdata)


def criar(__data:dict) -> bool:
    """
    Cria um jogo e automaticamente adciona a biblioteca do usuario.
    Tambem pode ser usado para atualizar um jogo

    __data: um dicionario contendo os dados do jogo

    __data.nome: nome do jogo (str)
    __data.username: o usuario que criou o jogo (str)
    __data.categoria: a categoria do jogo (str)
    __data.data: a data de lançamento do jogo (str)
    __data.tags: as tags do jogo (set)
    __data.privado: true se o jogo for privado (bool)
    __data.executavel: o caminho, ou comando para abrir o jogo
    """
    global id, PASTA

    utils.write(f'{PASTA}/{id}', __data)

    add_to_collection(__data, id)

    increment_id()


def validar(id) -> int:
    """
    Valida se o jogo é valido é valido para uso

    É valido caso o id seja um numero inteiro e o jogo á já foi
    criado antes e tenha os dados validos

    return 1: caso o id não seja um numero inteiro  
    return 2: caso o jogo não foi criado  

    return 0: caso seja valido
    """
    global PASTA
    
    if type(id) != int:
        if type(id) == str:
            try:
                int(id)
            except ValueError:
                return 1
        return 1

    if id not in os.listdir(PASTA):
        return 2

    return 0


def favoritar(id, username):
    """
    Adciona o jogo a lista de favorito do usuario

    id: o id unico do jogo
    username: o nome unico do usuario

    return 1: caso o id do jogo seja invalido
    return 2: caso o username seja invalido

    return 0: em sucesso
    """
    global PASTA

    USERPATH = user.PASTA+"/"+username

    userdata = utils.parser(USERPATH)

    # jogo não encontrado
    if validar() != 0:
        return 1
    
    # caso o usuario não seja valido
    if user.validar() != 0:
        return 2

    try:
        userdata["favoritos"].append(id)
    except KeyError:
        userdata["favoritos"] = [id]
    
    utils.write(USERPATH, userdata)



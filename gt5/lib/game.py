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


def make_path(id):
    global PASTA

    return PASTA+"/"+id


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

    # cria a pasta de jogos caso ainda não exista
    if PASTA not in os.listdir():
        os.mkdir(PASTA)

    utils.write(make_path(id), __data)

    # adciona a coleção do usuario
    #   usa o username em __data
    user.add_to_collection(__data["username"], id)

    # incrementa o id
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


def get(id):
    """
    Retorna os dados do jogo num dicionario
    """

    PATH = make_path(id)

    return utils.parser(PATH)


def list_games() -> list:
    """
    Lista todos os jogos registrados
    
    :return: o id dos jogos numa lista
    """
    global PASTA

    return os.listdir(PASTA)


def get_all_games(username=None) -> list:
    """
    Retorna todo os dados dos jogos registrados
    """
    games_data = list()

    for id in list_games():
        jogo = get(id)

        # caso seja o dono do jogo
        if jogo["username"] == username:
            jogo["owner"] = True
        else:
            jogo["owner"] = False

        # caso o jogo esteja nos favoritos
        if username and id in user.get_favoritos(username):
            jogo["favorito"] = True
        else:
            jogo["favorito"] = False

        games_data.append(jogo)

    return games_data
    


def get_accessible_game(username:str=None) -> dict:
    """
    Retorna os jogos acessiveis ao usuario
    """

    games = list()

    # para cada jogo
    for jogo in get_all_games(username):

        # caso pertença ao usuario ou seja publico
        if jogo["username"] == username or not jogo["private"]:
            games.append(jogo)

    return games


def remove(id):
    # remove o jogo da coleção do usuario
    user.remove_collection(get(id)["username"], id)

    # deleta o arquivo
    os.remove(make_path(id))


def pesquisar(key=None, value=None):
    """
    Pesquisa todas os ocurencias correspondente aos argumentos.

    :param key: pesquisa pelo atributo do jogo como nome por exemplo
    :param value: pesquisa pelo valor do atributo

    Caso o key seja uma lista o value tambem deverá ser uma lista com o
    mesmo tamanho.
    Quando a pesquisa é feita usando lista ela é uma pesquisa multipesquisa.
    e o jogo precisa satisfaser todos os requisitos para ser uma pesquisa
    valida.

    ex: nome="Jogo teste 1"
        -key-|----value----
    """

    # pesquisa todos os jogos
    todos_os_jogos = get_all_games()

    resultado = list()

    # faz o error checking
    if type(key) == str and type(value) == str:
        for jogo in todos_os_jogos:
            if jogo[key] == value:
                resultado.append(jogo)
    elif len(key) == len(value):
        keys = key
        values = value
        for jogo in todos_os_jogos:
            # o jogo precisar passar todos os testes 
            teste = True
            for key, value in keys, values:
                if jogo[key] != value:
                    teste = False
            if teste:
                resultado.append(jogo)
    
    return resultado


def delete_by_key(key:str, value) -> None:
    """
    Faz uma pesquisa e deleta os arquivos que a pesquisa retorna
    """
    resultado = pesquisar(key, value)

    for jogo in resultado:
        remove(jogo["id"])


def get_categoria(username:str=None) -> dict:
    jogos = get_accessible_game(username)

    resultado = dict()

    for jogo in jogos:
        if jogo["categoria"] not in resultado:
            resultado[jogo["categoria"]] = [jogo]
        else:
            resultado[jogo["categoria"]].append(jogo)


def get_my_games(username:str) -> dict:
    """
    Retorna os dados dos jogos que o usuario criou
    """
    resultado = list()

    for jogo in get_all_games(username):
        if jogo["username"] == username:
            resultado.append(jogo)
    
    return resultado


def get_favoritos(username:str) -> list:
    """
    Retorna os dados dos jogos favoritos do usuario
    """
    resultado = list()


    for jogo in get_all_games(username):
        if jogo["favorito"]:
            resultado.append(jogo)
    
    return resultado


def delete_by_user(username:str) -> None:
    """
    Deleta todos os jogos criado pelo usuario
    """
    delete_by_key("username", username)

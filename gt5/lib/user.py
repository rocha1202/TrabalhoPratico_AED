"""
Cria e gere usuarios
"""

import os
from os import path

if __name__ == "__main__":
    import utils
    import game
else:
    from lib import utils
    from lib import game

PASTA = 'users' # a pasta que contem os usuarios
CONFIGFILE = '.config' # o nome do arquivo de configuração que contem os dados do usuario
COLLECTIONFILE = 'collection.txt' # arquivo de configuração de coleção
FAVORITESFILE = 'favorites.txt' # o arquivo de configuração para os favoritos
THEMEFILE = 'theme.config' # o arquivo de configuração do thema do usuario
LOGINFILE = 'login.cache' # o arquivo cache de login
LOGINPATH = f'{PASTA}/{LOGINFILE}'


def User(username:str, nome:str, palavrapasse:str, administrador:bool=False) -> dict:
    """
    Cria o objeto user (não é uma classe)
    """
    return {username: username, nome:nome, palavrapasse:utils.criptografar(palavrapasse), administrador:administrador}


def user_path(username:str) -> str:
    """
    retorna o caminho para a pasta pessoal do usuario
    """
    global PASTA
    return PASTA+"/"+username


def __file_in_user(username:str, __file:str) -> str:
    """
    retorna o caminho do arquivo na pasta de usuario
    """
    return user_path(username)+"/"+__file


def config_path(username: str) -> str:
    """
    retorna o caminho para o arquivo de configuração do usuario
    """
    global CONFIGFILE

    return __file_in_user(username, CONFIGFILE)


def collection_path(username:str) -> str:
    """
    retorna o cominho para a coleção do usuario
    """
    global COLLECTIONFILE

    return __file_in_user(username, COLLECTIONFILE)


def favorites_path(username:str) -> str:
    """
    retorna o caminho para os favoritos do usuario
    """
    global FAVORITESFILE

    return __file_in_user(username, FAVORITESFILE)


def theme_path(username:str) -> str:
    """
    retorna o caminho para o tema customizado do usuario
    """
    global THEMEFILE

    return __file_in_user(username, THEMEFILE)


def user_paths(username:str) -> str:
    """
    retorna o caminho de todos os ficheiros do usuario
    """
    return config_path(username), collection_path(username), favorites_path(username), theme_path(username)


def make_user_files(username:str) -> int:
    """
    Criar os arquivos do usuario
    """
    USERPATH, COLLECTIONPATH, FAVORITESPATH, THEMEFILE = user_paths(username)

    # caso a pasta users/ não exista
    if path.exists(PASTA):
        os.mkdir(PASTA)
    
    # caso o usuario já exista
    if path.exists(USERPATH) :
        return 1, "usuario já existe"
    
    # cria os arquivos de configuração, coleção e favoritos
    utils.criar_ficheiro(USERPATH)
    utils.criar_ficheiro(COLLECTIONPATH)
    utils.criar_ficheiro(FAVORITESPATH)
    utils.criar_ficheiro(THEMEFILE)

    return 0; # sinaliza sucesso


def criar(username:str, nome:str, palavrapasse:str, administrador:bool=False) -> int:
    """
    cria um novo usuario, ou o atualiza os seus dados

    cria um arquivo na pasta users com o nome de 'username' com todos os dados
    do usuario

    :param username: nome unico de usuario
    :param nome: o nome real do usuario
    :param palavrapasse: a palavrapasse do usuario

    :return 1: caso o usuario já exista
    :return 0: caso sucesso
    """
    global PASTA
    
    # cria os arquivos e retorna erro caso não seja possivel
    fail = make_user_files(username)
    
    if fail:
        return fail

    USERPATH = user_path(username)
    
    user = User(username, nome, palavrapasse, administrador)
    
    # criar os arquivos do usuario

    # cria o ficheiro de configuração
    utils.write(USERPATH, user)

    
    return True


def get(username:str) -> dict:
    """
    Retorna os dados do usuario num dicionario
    """
    return utils.parser(user_path(username))


def delete(username:str) -> int:
    # caso validar retorne um valor igual a 1
    # sinalizando que o usuario não existe
    if validar(username) != 1:
        return validar(username)
    
    # deleta o diretorio do usuario
    os.remove(user_path(username))

    # deleta os seus jogos
    game.delete_by_user(username)


def validar(username:str):
    """
    Valida o usuario

    :return 1: caso o usario não foi resgistrado
    :return 2: caso não tenha um nome valido

    :return 0: caso seja valido
    """

    # usuario não registrado
    if username not in os.listdir(PASTA):
        return 1, "Usuario não registrado"
    
    userdata = utils.parser(PASTA+"/"+username)
    
    # caso não tenha um nome
    if not userdata["nome"]:
        return 2, "nome invalido"
    
    return 0


def collection_file(username:str) -> str:
    """
    Retorna o caminho para o arquivo da coleção dos usuarios
    """
    global COLLECTIONFILE

    return __file_in_user(username, COLLECTIONFILE)


def add_collection(username:str, game_id:int):
    """
    Adciona o jogo a coleção do usuario
    """

    game_id = list(game_id)

    utils.write_list(collection_file(username), game_id)


def get_collection(username:str) -> list:
    """
    Retorna os jogos na coleção do usuario
    """

    return utils.parse_list(collection_file(username))


def remove_collection(username:str, gameid:id) -> None:
    """
    Remove o jogo da coleção do usuario
    """
    global COLLECTIONFILE

    PATH = __file_in_user(username, COLLECTIONFILE)

    with open(PATH, "w") as file:
        try:
            # lê o arquivo e remove o id do arquivo e volta a o escrever
            file.write(";".join(set(file.read().split(";")).remove(str(gameid))))
        # ignora caso não exista
        except KeyError:
            pass


def favoritos_file(username:str) -> str:
    """
    Retorna o caminho para o arquivo dos favoritos do usuario
    """
    global FAVORITESFILE

    return __file_in_user(username, FAVORITESFILE)


def favoritar(game_id:int|str, username:str) -> None:
    """
    Adciona o jogo a lista de favorito do usuario
    """

    game_id = list(game_id)

    utils.write_list(favoritos_file(username), game_id)


def get_favoritos(username:str):
    """
    Retorna os favoritos do usuario
    """
    return utils.parse_list(favoritos_file(username))



def remover_favoritos(game_id:int|str, username:str) -> None:
    """
    Remove o jogo da lista dos favoritos
    """
    utils.delete_list(favoritos_file(username), game_id)


def cache_login(username:str) -> str:
    """
    Cria um ficheiro com os dados da ultima secção
    """
    global LOGINPATH

    utils.write(LOGINPATH, {"username":username})


def get_login() -> str:
    """
    Retorn o login em cache
    """
    global LOGINPATH

    # caso o arquivo não exista
    if not path.exists(LOGINPATH):
        return None
    
    return utils.parser(LOGINPATH)["username"]


def delete_login_cache() -> None:
    """
    Deleta o cache do login
    """
    global LOGINPATH

    if not path.exists(LOGINPATH):
        return None
    
    return utils.write(LOGINPATH, {"username": False})


def login(username:str, password:str, remeber:bool) -> int:
    """
    Faz o login da conta

    :return 1: caso o usuario não já foi regitrado
    :return 2: caso o nome não seja valido
    :return 3: caso a palavrapasse seja invalida

    :return 0: caso sucesso
    """

    # verifica se o usuario existe
    # validar retorna 0 caso seja valido
    if validar(username) != 0:
        return validar
    
    if get(username)["password"] != password:
        return
    
    if remeber:
        cache_login(username)

    return 0

class utilizador:
    f =open("./users/USER-ATIVO","r")
    linha=f.readlines()
    print(linha)
    f.close

if __name__ == "__main__":
    criar("filintodelgado", "Filinto Delgado", "1234")
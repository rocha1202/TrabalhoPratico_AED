"""
Cria e gere usuarios
"""

import os

if __name__ == "__main__":
    import utils
else:
    from lib import utils

PASTA = 'users' # a pasta que contem os usuarios


def criar(username:str, nome:str, palavrapasse:str) -> bool:
    """
    cria um novo usuario, ou o atualiza os seus dados

    cria um arquivo na pasta users com o nome de 'username' com todos os dados
    do usuario

    username: nome unico de usuario
    """
    global PASTA

    # O usuario já existe
    if username in os.listdir(PASTA):
        return 1
    
    userdata = {"nome": nome, "palavrapasse": palavrapasse}

    utils.write(PASTA+"/"+username, userdata)    
    
    return True


def validar(username:str):
    """
    Valida o usuario

    return 1: caso o usario não foi resgistrado
    return 2: caso não tenha um nome valido

    return 0: caso seja valido
    """
    global PASTA

    # usuario não registrado
    if username not in os.listdir(PASTA):
        return 1
    
    userdata = utils.parser(PASTA+"/"+username)
    
    # caso não tenha um nome
    if not userdata["nome"]:
        return 2
    
    return 0


if __name__ == "__main__":
    criar("filintodelgado", "Filinto Delgado", "1234")
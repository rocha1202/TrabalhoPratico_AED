"""
Os utilitarios do GT5.

Contem funções basicas, genericas e utilitarios
"""

CONFIGPATH = ".config/.config"


def criar_ficheiro(__file:str) -> bool:
    """
    cria um ficheiro

    :return True: caso o arquivo seja criaro
    :return False: em caso de erro
    """
    try:
        open(__file, "x").close()
    except:
        return False

    return True


def __formatline(key: str, value:str):
    """
    Formata uma linha baseado no key e value provido

    !! desenhado para ser usado pela função save
    !! não deve ser usado diretamente
    """
    text = f'{key}='

    # embrulha com o " só se não for um numero
    if type(value) == str:
        text += "\""

    # se o valor é uma lista ou um set vamos guardar no formato
    # comma-separeted value (value;value;value)
    if type(value) == list or type(value) == set or type(value) == tuple:
        for item in value:
            text += f'{item};'
        
        text = text[:-1] # remove o ultimo ponto e virgula (;)
    else:
        text += f'{value}'

    if type(value) == str:
        text += "\""
    
    text += '\n' # adciona uma quebra de linha no fim

    return text


def parser(__filepath:str) -> dict:
    """
    Lê o arquivo e converte o conteudo para um dicionario
    """
    results = dict()

    with open(__filepath, "r") as file:
        # lê linha a linha
        for line in file:
            # ignora comentarios e as linhas invalidas
            if line[0] == "#" or len(line.split("=")) < 2:
                continue
            
            # separa a chave do valor
            key, value = line.split("=")
            # faz a sanatização dos dados
            key.strip()
            value.strip()
            
            new_value = ""

            # remove os caracters extras no value como a nova linha(\n) e os apostrofes ("")
            for i in range(len(value)):
                caracter = value[i]

                # remove as novas linhas
                if caracter == "\n":
                    continue

                # ignora o caracter com 'escapado' (ex: \")
                if i > 0 and value[i - 1] == "\\":
                    continue

                # remove os caracters extras
                if caracter == "\"" or caracter == "\'":
                    continue

                new_value += caracter
            
            new_value.strip()

            # caso seja uma lista
            if new_value.count(";") != 0:
                new_value = new_value.split(";")
            
            if new_value == "True":
                new_value = True
            
            if new_value == "False":
                new_value = False
            
            # converte para inteiro se possivel
            try:
                new_value = int(new_value)
            except TypeError:
                pass
            except ValueError:
                pass

            # guarda no dicionario
            results[key] = new_value

        # Retorn defaults caso este exita
        return results if results else dict()


def write(__filepath:str, __data:dict) -> bool:
    """
    Guarda os dados providos ao ficheiro provido preservando os
    comentarios. Os dados que não foram providos como argumentos
    tambem são preservados. Caso o arquivo não exista ele é criado.
    Escreve tambem um conjunto de comentarios no arquivo descrevendo
    o uso

    __filepath: o caminho do arquivo onde os dados serão guardados,
    cria um novo caso não exista

    __dada: os dados a serem guardados que devem ser um dicionario
    """

    # esses comentarios servem para ajudar 
    COMENTARIOS = """# ----------------------------------------
# comentarios gerados automaticamente
# ----------------------------------------
# os comentarios começam com um jogo da velha (#)
# seguem uma estrutura de key=value
# value deve ser embrulhado em aspas duplas ("") quando for uma string
# o valor pode ser string, lista (list, tuple, set), 
# booleano (True, False) ou numero interio
# recomendado não conter espaços entre eles
# ----------------------------------------
"""

    chaves = __data.keys() # as chaves nos dados
    text = COMENTARIOS # o que vai ser reescrito depois no arquivo
    value = "" # calor em cada loop
    key = "" # chave em cada loop

    try:
        open(__filepath, "x")
    # caso o arquivo já exista
    except:
        for key in __data:
            text += __formatline(key, __data[key])
    else:
        with open(__filepath, "r") as file:
            # atualiza os dados existentes
            for line in file:
                if line.startswith("#"):
                    text += line
                    continue # ignora comentarios

                line_content = line.split("=")

                # caso a chave já exista o atualiza
                if key in chaves:
                    value = __data[line_content[0]]
                    __formatline(key, value)
                    continue
                
                text += line # conserva a linha
            
            # caso existam ainda dados no dicionario os escreve abaixo
            for key in __data:
                # escreve os restantes
                text += __formatline(key, __data[key])
    
    # reescreve o texto modificado
    with open(__filepath, "w") as file:
        file.write(text)


def write_list(__path:str, __list:list) -> None:
    """
    Escreve uma lista a um arquivo no formato "value;value"
    """
    __list = set(__list)

    with open(__path, "a") as file:
        file.write(";".join(__list))


def parse_list(__path:str) -> list:
    """
    Lê um arquivo e converte para uma lista.
    """

    with open(__path, "r") as file:
        # lê o arquivo
        # separa os elementos
        # converte para set para evitar duplicações
        # converte novamente para lista e retorna
        return list(set(file.read().split(";")))


def delete_list(__path:str, __value:str|int) -> None:
    """
    Deleta um valor de uma arquivo do tipo lista
    """
    # lê o arquivo
    # transforma numa lista
    # remove a primeira ocorencia do __value
    # reescreve o arquivo com os dados alterados
    write_list(parse_list(__path).remove(__value))
    

def get_defaults():
    return parser(CONFIGPATH)


def get_app_name():
    return get_defaults()["app_name"]


DEFAULT = get_defaults()
config = get_defaults()

APPNAME = config["app_name"]
theme   = config["theme"]


def criptografar(palavrapasse:str) -> str:
    """
    criptografa a palavrapasse criando um hash
    """
    return palavrapasse


if __name__ == "__main__":
    # ao rodar o programa diretamente este imprime na tela as definições padrões
    print(parser(CONFIGPATH))
    write("test", {"person": [12, 42], "age": 18})


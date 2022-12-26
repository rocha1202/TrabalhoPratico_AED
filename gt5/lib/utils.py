"""
Os utilitarios do GT5.

Contem funções basicas, genericas e utilitarios
"""

CONFIGPATH = ".config/.config"


def __writeline(key: str, value:str):
    """
    Formata uma linha baseado no key e value provido

    !! desenhado para ser usado pela função save
    !! não deve ser usado diretamente
    """
    text = f'{key}=\"'
    # se o valor é uma lista ou um set vamos guardar no formato
    # comma-separeted value (value;value;value)
    if type(value) == list or type(value) == set:
        for item in value:
            text += f'{item};'
        
        text = text[:-1] # remove o ultimo ponto e virgula (;)
    else:
        text += f'{value}'
    
    text += '\"\n' # adciona uma quebra de linha

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
    tambem são preservados. Caso o arquivo não exista ele é criado

    __filepath: o caminho do arquivo onde os dados serão guardados,
    cria um novo caso não exista

    __dada: os dados a serem guardados que devem ser um dicionario
    """
    chaves = __data.keys() # as chaves nos dados
    text = "" # o que vai ser reescrito depois no arquivo
    value = "" # calor em cada loop
    key = "" # chave em cada loop

    try:
        open(__filepath, "x")
    # caso o arquivo já exista
    except:
        for key in __data:
            text += __writeline(key, __data[key])
    else:
        with open(__filepath, "r") as file:
            # atualiza os dados existentes
            for line in file:
                if line.startswith("#"):
                    text += line
                    continue # ignora comentarios

                line_content = line.split("=")


                # caso já exista o atualiza
                if key in chaves:
                    value = __data[line_content[0]]
                    __writeline(key, value)
                    continue
                
                text += line # conserva a linha
            
            # caso existam ainda dados no dicionario os escreve abaixo
            for key in __data:
                # escreve os restantes
                text += __writeline(key, __data[key])
    
    # reescreve o texto modificado
    with open(__filepath, "w") as file:
        file.write(text)


def get_defaults():
    return parser(CONFIGPATH)


def get_app_name():
    return get_defaults()["app_name"]


DEFAULT = get_defaults()
config = get_defaults()

APPNAME = config["app_name"]
theme   = config["theme"]


if __name__ == "__main__":
    # ao rodar o programa diretamente este imprime na tela as definições padrões
    print(parser(CONFIGPATH))
    write("test", {"person": [12, 42], "age": 18})
    print(parser("test"))


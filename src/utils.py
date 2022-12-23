"""
Os utilitarios do GT5.

Contem funções basicas, genericas e utilitarios
"""

config_file = ".config"

def get_default() -> dict:
    """
    Retorna as configurações padroẽs definidas no arquivo 'config_file'

    Por padrão o arquivo é .config
    """
    defaults = dict()

    with open(config_file, "r") as file:
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


                # remove os caractrs extras
                if caracter == "\"" or caracter == "\'":
                    continue

                new_value += caracter

            # guarda no dicionario
            defaults[key] = new_value.strip()

        # Retorn defaults caso este exita
        return defaults if defaults else dict()
    

if __name__ == "__main__":
    # ao rodar o programa diretamente este imprime na tela as definições padrões
    print(get_default())

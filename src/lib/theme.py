"""
Define metodos para uso de temas no programa
"""

import lib.utils as utils

default_theme_path = ".theme"


def get_default_theme()->dict:
    """
    retorna a palleta de cores padrão em formato de dicionario
    """

    return utils.parser(default_theme_path)


if __name__ == "__main__":
    print(get_default_theme())
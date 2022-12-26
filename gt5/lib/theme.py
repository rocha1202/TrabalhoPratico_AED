"""
Define metodos para uso de temas no programa
"""

from sys import argv

# importa dinamicamente
if __name__ == "__main__":
    import utils
    from utils import APPNAME
    from utils import theme as current_theme_path
else:
    import lib.utils as utils
    from lib.utils import APPNAME
    from lib.utils import theme as current_theme_path


__DEFAULT_THEME_PATH = ".config/theme.config" # o arquivo que contem o tema padrão

__PROGRAMNAME = "themes-gt5" # o nome do utilitario
__DEFAULT     = True if utils.theme == __DEFAULT_THEME_PATH else False


def get_theme(__path: str) -> dict:
    """
    retorna a palleta de cores especificado em um dicionario
    """

    return utils.parser(__path)


def get_default_theme() -> dict:
    """
    retorna a palleta de cores padrão em um dicionario
    """
    
    return get_theme(__DEFAULT_THEME_PATH)


def print_help() -> None:
    """
    impreme uma tela de ajuda do utilitario
    """
    global __PROGRAMNAME, APPNAME

    print(f'{__PROGRAMNAME}: utilitario de temas para o \'{APPNAME}\'.')
    print()
    print("Quando chamado sem argumentos impreme o tema de cores em uso no teminal")
    print()
    print(f'Argumentos: ')
    print(f'\t[--default|-d] - impreme o tema padrão')


def print_theme(theme_name:str, colors:dict) -> None:
    """
    imprime as cores do tema em hexadecimal (#000000) no console
    """
    print(f'Tema {theme_name}:')
    
    for color in colors:
        print(f'\t{color} - {colors[color]};')


DEFAULT_THEME = get_default_theme()
current_theme = DEFAULT_THEME if __DEFAULT else get_theme(current_theme_path)


def print_default_theme() -> None:
    """
    Impreme as cores padrões do app no console em hexadecimal (#000000)
    """

    global DEFAULT_THEME

    print_theme("Padrão", DEFAULT_THEME)


def print_current_theme() -> None:
    """
    Impreme a paleta de cores em uso no terminal
    """

    print_theme(f'em uso ({"Padrão" if __DEFAULT else ""})', current_theme)


# quando o programa é rodado diretamente
if __name__ == "__main__":
    if len(argv) == 1:
        print_current_theme()
    elif len(argv) == 2:
        match argv[1]:
            case "--default":
                print_default_theme()
            case "-d":
                print_default_theme()
            case _:
                print_help()

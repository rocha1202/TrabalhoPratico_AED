import customtkinter
from lib import utils, user, theme, game
from widgets import logo, button, frame, tabs
from lib import log
from window import add
import app

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

APPNAME = "GT5 - Detalhes do Jogo"


def App() -> customtkinter.CTk:
    """
    Criar a window de detalhes do jogo
    """

    # cria a window e aplica a cor de fundo
    window = customtkinter.CTkToplevel(app.DEFAULTAPP, fg_color=theme.current_theme["PRINCIPAL"])

    # armazena o tema para ser usado
    window.current_theme = theme.current_theme

    # configura a window
    window.title(APPNAME) # o titulo do app
    # self.geometry(f"{1540}x{1024}") # o tamanho inicial
    # self.minsize(1540, 1024) # tamanho minimo
    
    # Maximiza a window
    # mas como não funciona em todos os sistemas devemos estar preparados
    # try:
    #     self.attributes("-zoomed", True) # maximiza o window
    # except:
    #     print(f'{APPNAME}: erro maximizando o app')
    #     # self.attributes("-fullscreen", True) # fullscreen no macos
    
    # configura a grid
    window.grid_columnconfigure(0, weight=1, pad=30)
    window.grid_rowconfigure((0, 1), pad=30)
    window.geometry("1000x600")

    # Torna impossivel aumentar ou diminuir a window
    window.resizable(0, 0)



    # configura o icone
    # self.iconbitmap("img/assets/gt5/logo-gt5.ico")

    return window
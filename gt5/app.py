import customtkinter
from lib import utils, user, theme, game
from widgets import logo, button, frame, tabs
from lib import log
from window import add

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

APPNAME = utils.APPNAME if utils.APPNAME else "GT5"


# isso é ainda só um placeholder do programa 
def App() -> customtkinter.CTk:
    """
    Criar a principal window do programa
    """
    # cria a window e aplica a cor de fundo
    window = customtkinter.CTk(fg_color=theme.current_theme["PRINCIPAL"])

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

    # coloca o logo no topo
    window.logo = logo.Logo(window)
    window.logo.grid(row=0, column=0)
    
    # o login
    window.login = "filintodelgado"

    # configura a fonte
    # self.font = customtkinter.CTkFont()

    # Torna impossivel aumentar ou diminuir a window
    window.resizable(0, 0)

    # configura o icone
    # self.iconbitmap("img/assets/gt5/logo-gt5.ico")

    # Cria o navbar em tabview
    window.tabview = tabs.Tabs(window, theme=window.current_theme, login=window.login)
    window.tabview.grid(row=1, column=0)

    window.menu = frame.MenuButtons(window)
    window.menu.grid(row=2, column=0, sticky="nesw", padx=10, pady=10)

    log.set_notification_display(window.menu.notification)

    return window
        
    
def restart(window):
        """
        Restart the tab view
        """
        window.tabview.destroy()
        window.tabview = tabs.Tabs(window, window.current_theme, login=window.login)
        window.tabview.grid(row=1, column=0)

def refresh(window):
        current_tab = window.tabview.get()

        # reseta e volta ao tab selecionado
        window.restart()
        window.tabview.set(current_tab)
        

# o programa só roda se for rodado diretamente
if __name__ == "__main__":
    app = App()
    app.mainloop()
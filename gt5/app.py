import customtkinter
from lib import utils, user, theme, game
from pages import tabs
from widgets import logo, button, frame

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

APPNAME = utils.APPNAME if utils.APPNAME else "GT5"


# isso é ainda só um placeholder do programa 
class App(customtkinter.CTk):
    def __init__(self):
        # armazena o tema para ser usado
        self.current_theme = theme.current_theme

        super().__init__(fg_color=self.current_theme["PRINCIPAL"]) # aplica a cor de fundo

        # configura a window
        self.title(APPNAME) # o titulo do app
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
        self.grid_columnconfigure(0, weight=1, pad=30)
        self.grid_rowconfigure((0, 1), pad=30)

        # coloca o logo no topo
        self.logo = logo.Logo(self)
        self.logo.grid(row=0, column=0)
        
        # o login
        self.login = "filintodelgado"

        # configura a fonte
        # self.font = customtkinter.CTkFont()

        # Torna impossivel aumentar ou diminuir a window
        self.resizable(0, 0)

        # configura o icone
        # self.iconbitmap("img/assets/gt5/logo-gt5.ico")

        # Cria o navbar em tabview
        self.tabview = tabs.Tabs(self, theme=self.current_theme, login=self.login)
        self.tabview.grid(row=1, column=0)

        self.menu = frame.MenuButtons(self)
        self.menu.grid(row=2, column=0, sticky="nesw", padx=10, pady=10)
    
    def restart(self):
        """
        Restart the tab view
        """
        self.tabview.destroy()
        self.tabview = tabs.Tabs(self, self.current_theme, login=self.login)
        self.tabview.grid(row=1, column=0)

    def refresh(self):
        current_tab = self.tabview.get()

        # reseta e volta ao tab selecionado
        self.restart()
        self.tabview.set(current_tab)
        



# o programa só roda se for rodado diretamente
if __name__ == "__main__":
    app = App()
    app.mainloop()
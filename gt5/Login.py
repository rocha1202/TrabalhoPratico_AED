import customtkinter

from lib import utils, theme
from widgets import logo

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

APPNAME = utils.APPNAME if utils.APPNAME else "GT5"


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
        
        self.resizable(0, 0)

        # configura a grid
        self.grid_columnconfigure(0, weight=1, pad=30)
        self.grid_rowconfigure((0, 1), pad=30)

        # coloca o logo no topo
        self.logo = logo.Logo(self)
        self.logo.grid(row=0, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
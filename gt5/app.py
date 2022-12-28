import customtkinter
from lib import utils
from lib import user
from lib import theme
from pages import library
from PIL import ImageTk
import tkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

APPNAME = utils.APPNAME if utils.APPNAME else "GT5"


# isso é ainda só um placeholder do programa 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__(theme.current_theme["ESCURO"]) # aplica a cor de fundo

        # configura a window
        self.title(APPNAME) # o titulo do app
        self.geometry(f"{1540}x{1024}") # o tamanho inicial
        #self.minsize(1540, 1024) # tamanho minimo
        #self.attributes("-zoomed", True) # maximiza o window
        #self.resizable(0, 0)

        # configura o icone
        # self.iconbitmap("img/assets/gt5/logo-gt5.ico")

        self.library = library.Library(self)
        self.library.grid()



# o programa só roda se for rodado diretamente
if __name__ == "__main__":
    app = App()
    app.mainloop()
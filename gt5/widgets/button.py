"""
Todos os botões usados no programa
"""
import customtkinter
from PIL import Image

PASTA = "img/assets/"
IMAGENS = ["logo", "plus-sign", "library", "heart", "settings", "user"]


def makePath(imagem):
    global PASTA

    return PASTA + imagem + ".png"


class SideButton(customtkinter.CTkButton):
    def __init__(self, master, img_path, size):
        self.img = customtkinter.CTkImage(Image.open(img_path), size=size)
        super().__init__(master, fg_color="transparent", border_width=None, text="", corner_radius=0, image=self.img, hover=False)


class Home(SideButton):
    def __init__(self, master):
        self.img_path = makePath(IMAGENS[0])
        super().__init__(master, img_path=self.img_path, size=(90, 73))


class Plus(SideButton):
    def __init__(self, master):
        self.img_path = makePath(IMAGENS[1])
        super().__init__(master, self.img_path, size=(80, 80))


class Library(SideButton):
    def __init__(self, master):
        self.img_path = makePath(IMAGENS[2])
        super().__init__(master, self.img_path, size=(100, 82))


class Heart(SideButton):
    def __init__(self, master):
        self.img_path = makePath(IMAGENS[3])
        super().__init__(master, self.img_path, size=(84, 77))


class Settings(SideButton):
    def __init__(self, master):
        self.img_path = makePath(IMAGENS[4])
        super().__init__(master, self.img_path, size=(94, 100))
    

class User(SideButton):
    def __init__(self, master):
            self.img_path = makePath(IMAGENS[5])
            super().__init__(master, self.img_path, size=(100, 100))
    
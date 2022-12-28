import customtkinter
from PIL import Image
from tkinter import StringVar


class SearchBar(customtkinter.CTkEntry):
    def __init__(self, master, text_color, fg_color):
        self.textvariable = StringVar()
        self.image_path = "img/assets/search-icon.png"
        self.image = customtkinter.CTkImage(Image.open(self.image_path))
        self.font = customtkinter.CTkFont(size=50)
        super().__init__(master, width=1148, height=81, corner_radius=30, fg_color=fg_color, border_width=0,
                         placeholder_text="Escreva para pesquisar...", textvariable=self.textvariable, font=self.font,
                         text_color=text_color, placeholder_text_color=text_color
                         )
"""
Todos os botões usados no programa
"""
import customtkinter
from PIL import Image


class Button(customtkinter.CTkButton):
  def __init__(self, master, text, theme, command=None):
    super().__init__(master, text=text, fg_color=theme["PRINCIPAL"], hover_color=theme["SECUNDARIA"], command=command)

  def change_image(self, new_image):
    self.configure(image=new_image)


class ImageButton(customtkinter.CTkButton):
  def __init__(self, master, fg_color, path, size=(10, 10), command=None):
    self.image = customtkinter.CTkImage(Image.open(path), size=size)
    super().__init__(master, fg_color=fg_color, text="", image=self.image, command=command,
                     width=size[0]+5, height=size[1]+5)
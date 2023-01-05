"""
Todos os botões usados no programa
"""
import customtkinter
from PIL import Image


ASSETPASTA = "img/assets/" # a pasta onde os assets se encontram


def make_image(__path:str, size:set=(10, 10)) -> customtkinter.CTkImage:
  """
  Retorna um CTkImage
  """
  return customtkinter.CTkImage(Image.open(__path), size=size)


def asset_path(name:str) -> str:
  """
  Retorna o caminho para o asset na pasta ASSETPASTA

  :param name: o nome do asset sem a extensão (ex: .png)
  """
  global ASSETPASTA

  return f'{ASSETPASTA}/{name}.png'


def make_asset(name:str, size:set=(10, 10)) -> customtkinter.CTkImage:
  """
  Retorna um CTkImage de um asset

  :param name: o nome do asset sem a sua extensão (ex: .png)
  :return: um imagem CtkImage já aberto e pronto para uso
  """
  return make_image(asset_path(name), size)



class Button(customtkinter.CTkButton):
  """
  O botão padrão do app, usando a cor principal para cor de fundo e a cor secundario no hover
  """
  def __init__(self, master, text, theme, command=None):
    super().__init__(master, text=text, fg_color=theme["PRINCIPAL"], hover_color=theme["SECUNDARIA"], command=command)

  def change_image(self, new_image):
    self.configure(image=new_image)


class ImageButton(customtkinter.CTkButton):
  """
  Botão de imagem principal do programa

  :param master: onde o widget vai ser posicionado
  :param name: o nome do asset sem a extensão .png
  :param size: o tamanho do asset
  :param comand: o função que será chamada quando o botão for clicado
  """
  def __init__(self, master, fg_color, name, size=(10, 10), command=None):
    super().__init__(master, fg_color=fg_color, text="", image=make_asset(name), command=command,
                     width=size[0]+5, height=size[1]+5)
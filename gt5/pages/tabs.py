import customtkinter
from lib import game, theme, user, utils
from widgets import frame


class Tabs(customtkinter.CTkTabview):
  """
  Cria o tab view do programa
  """
  def __init__(self, master:customtkinter.CTk, theme, login):
    super().__init__(master, fg_color=theme["ESCURO"], segmented_button_selected_color=theme["PRINCIPAL"], 
                     segmented_button_selected_hover_color=theme["ESCURO"])
    self.jogos = self.add("Jogos")
    self.collection = self.add("Coleção")
    self.favoritos = self.add("Favoritos")
    self.categorias = self.add("Categorias")
    self.listas = self.add("Listas")
    self.conta = self.add("Conta")

    self.tabs = [self.jogos, self.collection, self.favoritos, self.categorias,
                 self.listas, self.conta]

    ######Jogos######
    self.jogos.jogos = frame.Jogos(self.jogos, theme, game.get_accessible_game(login))
    self.jogos.jogos.pack(fill="both")

    ######Coleção#####
    self.collection.jogos = frame.Jogos(self.collection, theme, game.get_my_games(login))
    self.collection.jogos.pack(fill="both")

    ######Favorito#####
    self.favoritos.jogos = frame.Jogos(self.favoritos, theme, game.get_favoritos(login))
    self.favoritos.jogos.pack(fill="both")

    ######Categoria#####
    self.categoria = frame.Categorias(self.categorias, theme, game.get_categoria(login))
    self.categoria.pack(fill="both")


    ######Lista#####
    self.listas = frame.Lista(self.listas,theme)
    self.listas.pack(fill="both")


    ######CONTA#####
    self.conta = frame.Conta(self.conta,theme, user.get_login(), user.get_password())
    self.conta.pack(fill="both")

  def povoarjogos():
    pass
import customtkinter
from lib import game, theme, user, utils
from widgets import frame


def Tabs(master:customtkinter.CTk, theme, login) -> customtkinter.CTkTabview:
  """
  Cria o tab view do programa
  """
  tab = customtkinter.CTkTabview(master, fg_color=theme["ESCURO"], segmented_button_selected_color=theme["PRINCIPAL"], 
                    segmented_button_selected_hover_color=theme["ESCURO"])
  tab.jogos = tab.add("Jogos")
  tab.collection = tab.add("Coleção")
  tab.favoritos = tab.add("Favoritos")
  tab.categorias = tab.add("Categorias")
  tab.listas = tab.add("Listas")
  tab.conta = tab.add("Conta")

  tab.tabs = [tab.jogos, tab.collection, tab.favoritos, tab.categorias,
                tab.listas, tab.conta]

  ######Jogos######
  tab.jogos.jogos = frame.Jogos(tab.jogos, theme, game.get_accessible_game(login))
  tab.jogos.jogos.pack(fill="both")

  ######Coleção#####
  tab.collection.jogos = frame.Jogos(tab.collection, theme, game.get_my_games(login))
  tab.collection.jogos.pack(fill="both")

  ######Favorito#####
  tab.favoritos.jogos = frame.Jogos(tab.favoritos, theme, game.get_favoritos(login))
  tab.favoritos.jogos.pack(fill="both")

  ######Categoria#####
  tab.categoria = frame.Categorias(tab.categorias, theme, game.get_categoria(login))
  tab.categoria.pack(fill="both")


  ######Lista#####
  tab.listas = frame.Lista(tab.listas,theme)
  tab.listas.pack(fill="both")


  ######CONTA#####
  tab.conta = frame.Conta(tab.conta,theme, user.get_login(), user.get_password())
  tab.conta.pack(fill="both")

  return tab

  def povoarjogos():
    pass
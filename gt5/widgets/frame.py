import customtkinter

from widgets import label, button


class ContentFrame(customtkinter.CTkFrame):
  def __init__(self, master, fg_color="transparent"):
    super().__init__(master, fg_color=fg_color, corner_radius=10)


class GameButtons(customtkinter.CTkFrame):
  """
  Adciona os botões de menu ao jogo

  Botão de editar: caso o usuario seja dono do jogo ele poderá editar o jogo
  Botão de delete: caso o usuario seja dono do jogo ele pode o deletar
  """
  def __init__(self, master, jogo):
    """
    :param master: o objeto master onde o widget vai ser posiciondo
    :param jogo: o objeto (dicionario) do jogo onde ele vai ser adcionado
    """
    super().__init__(master, fg_color="transparent")

    self.grid_columnconfigure((0, 1, 2, 3), pad=10)

    self.favoritar_name = "heart-filled" if jogo["favorito"] else "heart"

    self.favoritar = button.ImageButton(self, fg_color="#293540", name=self.favoritar_name, command=self.favoritarJogo)
    self.favoritar.grid(column=2, row=0)

    if jogo["owner"]:
      self.edit = button.ImageButton(self, fg_color="green", name="editar")
      self.edit.grid(column=1, row=0)
      self.delete = button.ImageButton(self, fg_color="red", name="delete")
      self.delete.grid(column=0, row=0)
    
    if jogo["command"]:
      self.command = button.ImageButton(self, fg_color="blue", name="play")
      self.command.grid(column=3, row=0)
    
  def favoritarJogo(self) -> None:
    self.favoritar_name = "heart-filled" if self.favoritar_name == "heart" else "heart"

    self.favoritar.configure(image=button.make_asset(self.favoritar_name))


class MenuButtons(customtkinter.CTkFrame):
  """
  Adciona um menu 
  """
  def __init__(self, master):
    super().__init__(master)

    self.grid_columnconfigure((0, 2), weight=0)
    self.grid_columnconfigure(1, weight=1, pad=10)

    # refresh
    self.refresh = button.ImageButton(self, fg_color="blue", name="refresh", size=(17, 15))
    self.refresh.grid(column=0, row=0, padx=10, pady=10)

    # notificações
    self.notification = customtkinter.CTkLabel(self, text="Nenhuma notificação por agora.", corner_radius=10)
    self.notification.grid(column=1, row=0)

    # add
    self.add = button.ImageButton(self, fg_color="green", name="plus-sign", size=(15,15))
    self.add.grid(column=2, row=0, padx=10)


class Jogo(ContentFrame):
  def __init__(self, master, jogo, theme):
    super().__init__(master, fg_color=theme["PRINCIPAL"])

    # configura a grid
    self.grid_columnconfigure(0, weight=1, pad=10)
    self.grid_columnconfigure(1, weight=0)

    # o nome do jogo
    self.name = label.GameTitle(self, text=jogo["nome"], theme=theme)
    self.name.grid(column=0, row=0, padx=10, sticky="w")

    if jogo["owner"] or jogo["command"]:
      self.buttons = GameButtons(self, jogo)
      self.buttons.grid(column=1, row=0, padx=10)


class Jogos(ContentFrame):
  def __init__(self, master, theme, jogos=None):
    super().__init__(master)

    self.todos_os_jogos = list()

    if jogos:
      if type(jogos) == list:
        for jogo in jogos:
          self.todos_os_jogos.append(Jogo(self, jogo, theme))
          self.todos_os_jogos[-1].pack(fill="x", pady=2)
      if type(jogos) == dict:
        self.todos_os_jogos.append(Jogo(self, jogos, theme))
        self.todos_os_jogos[-1].pack(fill="x")
    else:
      self.info = label.GameTitle(self, text="Nenhum jogo para mostrar...", theme=theme)
      self.info.pack()


class Categoria(ContentFrame):
  def __init__(self, master, theme, nome, jogos):
    super().__init__(master, theme["PRINCIPAL"])
    self.configure(corner_radius=10)

    self.titulo = label.GameGenre(self, nome, theme)
    self.titulo.pack(pady=2, padx=5)

    self.jogos = Jogos(self, theme, jogos)
    self.jogos.pack(fill="both", pady=2, padx=2)
  
class Categorias(ContentFrame):
  """
  {
    "categoria1": [
      jogo1, jogo2, jogo3
    ],
    "categoria2": [
      jogo4, jogo5, jogo6
    ]
  }

  ["categoria1", "categoria2"]
  """
  def __init__(self, master, theme, jogos):
    super().__init__(master)

    self.categorias = []

    for categoria in jogos.keys():
      self.categorias.append(Categoria(self, theme, categoria.upper(), jogos[categoria]))
      self.categorias[-1].pack(fill="both", pady=10)













class Favorite:
  pass
import customtkinter

from widgets import label, button
from lib import user
from lib import log
from window import add

def ContentFrame(master, fg_color="transparent") -> customtkinter.CTkFrame:
  """
  Criar o frame padrão do app
  """
  return customtkinter.CTkFrame(master, fg_color=fg_color, corner_radius=10)

def GameButtons(master, jogo) -> customtkinter.CTkFrame:
  """
  Adciona os botões de menu ao jogo

  Botão de editar: caso o usuario seja dono do jogo ele poderá editar o jogo
  Botão de delete: caso o usuario seja dono do jogo ele pode o deletar

  :param master: o objeto master onde o widget vai ser posiciondo
  :param jogo: o objeto (dicionario) do jogo onde ele vai ser adcionado
  """
  frame = ContentFrame(master, fg_color="transparent")

  frame.grid_columnconfigure((0, 1, 2, 3), pad=10)
  
  frame.jogo = jogo

  frame.favoritar_name = "heart-filled" if jogo["favorito"] else "heart"

  frame.favoritar = button.ImageButton(frame, fg_color="#293540", name=frame.favoritar_name, command=lambda:favoritarJogo(frame))
  frame.favoritar.grid(column=2, row=0)

  if jogo["owner"]:
    frame.edit = button.ImageButton(frame, fg_color="green", name="editar")
    frame.edit.grid(column=1, row=0)
    frame.delete = button.ImageButton(frame, fg_color="red", name="delete")
    frame.delete.grid(column=0, row=0)
  
  if jogo["command"]:
    frame.command = button.ImageButton(frame, fg_color="blue", name="play")
    frame.command.grid(column=3, row=0)
  
  return frame

    
def favoritarJogo(master) -> None:
  """
  Adciona ou remove o jogo da lista de favoritos do ususario
  """
  if master.favoritar_name == "heart-filled":
    master.favoritar_name = "heart"
    log.notification("Jogo removido dos favoritos")
    master.favoritar.configure(image=button.make_asset(master.favoritar_name))
  else:
    master.favoritar_name = "heart-filled"
    log.notification("Jogo adcionado dos favoritos")
    master.favoritar.configure(image=button.make_asset(master.favoritar_name))


def MenuButtons(master:customtkinter.CTk) -> customtkinter.CTkFrame:
    menu = customtkinter.CTkFrame(master)

    menu.grid_columnconfigure((0, 2), weight=0)
    menu.grid_columnconfigure(1, weight=1, pad=10)

    # refresh
    menu.refresh = button.ImageButton(menu, fg_color="blue", name="refresh", size=(17, 16), command=lambda: log.notification("Refresh"))
    menu.refresh.grid(column=0, row=0, padx=10, pady=10)

    # notificações
    menu.notification = customtkinter.CTkLabel(menu, text="Nenhuma notificação por agora.", corner_radius=10)
    menu.notification.grid(column=1, row=0)

    # add
    menu.add = button.ImageButton(menu, fg_color="green", name="plus-sign", size=(15,15), command=lambda: add_game(menu, master))
    menu.add.grid(column=2, row=0, padx=10)
    
    return menu

  
def add_game(menu, master:customtkinter.CTk):
  """
  Ao clicar no botão abre uma window para adcionar um novo jogo
  """
  menu.add_window = add.AddGame(master)


def Jogo(master, jogo, theme) -> customtkinter.CTkFrame:
  frame = ContentFrame(master, fg_color=theme["PRINCIPAL"])

  # configura a grid
  frame.grid_columnconfigure(0, weight=1, pad=10)
  frame.grid_columnconfigure(1, weight=0)

  # o nome do jogo
  frame.name = label.GameTitle(frame, text=jogo["nome"], theme=theme)
  frame.name.grid(column=0, row=0, padx=10, sticky="w")

  if jogo["owner"] or jogo["command"]:
    frame.buttons = GameButtons(frame, jogo)
    frame.buttons.grid(column=1, row=0, padx=10)
  
  return frame


def Jogos(master, theme, jogos=None) -> customtkinter.CTkFrame:
    frame = ContentFrame(master)

    frame.todos_os_jogos = list()

    if jogos:
      if type(jogos) == list:
        for jogo in jogos:
          frame.todos_os_jogos.append(Jogo(frame, jogo, theme))
          frame.todos_os_jogos[-1].pack(fill="x", pady=2)
      if type(jogos) == dict:
        frame.todos_os_jogos.append(Jogo(frame, jogos, theme))
        frame.todos_os_jogos[-1].pack(fill="x")
    else:
      frame.info = label.GameTitle(frame, text="Nenhum jogo para mostrar...", theme=theme)
      frame.info.pack()
    
    return frame


def Categoria(master, theme, nome, jogos) -> customtkinter.CTkFrame:
  categoria = ContentFrame(master, theme["PRINCIPAL"])

  categoria.configure(corner_radius=10)

  categoria.titulo = label.GameGenre(categoria, nome, theme)
  categoria.titulo.pack(pady=2, padx=5)

  categoria.jogos = Jogos(categoria, theme, jogos)
  categoria.jogos.pack(fill="both", pady=2, padx=2)

  return categoria


def Lista(master, theme) -> customtkinter.CTkFrame:
  lista = ContentFrame(master, theme["PRINCIPAL"])
  lista.configure(corner_radius=10)

  return lista


def Conta(master, theme, username, password) -> customtkinter.CTkFrame:
  conta = ContentFrame(master, theme["PRINCIPAL"])
  conta.configure(corner_radius=10)

  conta.username = customtkinter.CTkLabel(conta, text=username)
  conta.username.pack()

  conta.password_old = customtkinter.CTkEntry(conta, placeholder_text="Password Antiga", show="*")
  conta.password_old.pack(pady=3)

  conta.password_new = customtkinter.CTkEntry(conta, placeholder_text="Password Nova", show="*")
  conta.password_new.pack(pady=3)

  conta.password_newVerifica = customtkinter.CTkEntry(conta, placeholder_text="Password Nova Novamente", show="*")
  conta.password_newVerifica.pack(pady=3)
  
  conta.alterar = customtkinter.CTkButton(conta, text="Alterar")
  conta.alterar.pack(pady=3)

  return conta


def Categorias(master, theme, jogos):
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
  frame = ContentFrame(master)

  frame.categorias = []

  for categoria in jogos.keys():
    frame.categorias.append(Categoria(frame, theme, categoria.upper(), jogos[categoria]))
    frame.categorias[-1].pack(fill="both", pady=10)
  
  return frame
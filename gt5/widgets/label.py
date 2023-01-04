import customtkinter


class Label(customtkinter.CTkLabel):
  def __init__(self, master, text, text_color, fg_color="transparent"):
    super().__init__(master, text=text, fg_color=fg_color, text_color=text_color, anchor="e")


class GameTitle(Label):
  def __init__(self, master, text, theme):
    super().__init__(master, text=text, text_color=theme["BRANCO"])

class GameGenre(Label):
  def __init__(self, master, text, theme):
    super().__init__(master, text=text, text_color=theme["BRANCO"])


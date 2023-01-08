import customtkinter


def Label(master, text, text_color, fg_color="transparent") -> customtkinter.CTkLabel:
    return customtkinter.CTkLabel(master, text=text, fg_color=fg_color, text_color=text_color, anchor="e")


def GameTitle(master, text, theme) -> customtkinter.CTkLabel:
  return Label(master, text=text, text_color=theme["BRANCO"])


def GameGenre(master, text, theme) ->customtkinter.CTkLabel:
  return Label(master, text=text, text_color=theme["BRANCO"])


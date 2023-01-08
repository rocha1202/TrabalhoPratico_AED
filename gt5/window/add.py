import customtkinter

def AddGame(master:customtkinter.CTk) -> customtkinter.CTkToplevel:
  """
  Cria uma window para adcionar um novo jogo
  """
  window = customtkinter.CTkToplevel(master)
  window.focus_force()
  window.title("Adcionar jogo")
  window.geometry(f'500x300+{master.winfo_x()}+{master.winfo_y()}')
  
  return window
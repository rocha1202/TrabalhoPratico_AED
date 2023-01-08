import customtkinter
from PIL import Image

LOGOPATH = "img/assets/gt5/1000x317.png"

def Logo(master) -> customtkinter.CTkButton:
  logo = customtkinter.CTkButton(master)
  logo.image = customtkinter.CTkImage(Image.open(LOGOPATH), size=(200, 63))
  logo.configure(image=logo.image, text="", bg_color="transparent",
                    fg_color="transparent", hover=False)
  return logo
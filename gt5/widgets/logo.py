import customtkinter
from PIL import Image

LOGOPATH = "img/assets/gt5/1000x317.png"

class Logo(customtkinter.CTkButton):
  def __init__(self, master):
    self.image = customtkinter.CTkImage(Image.open(LOGOPATH), size=(200, 63))
    super().__init__(master, image=self.image, text="", bg_color="transparent",
                     fg_color="transparent", hover=False)
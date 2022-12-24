import tkinter
import tkinter.messagebox
import customtkinter
import lib.utils as utils
import lib.theme as theme

defaults_settings = utils.get_defaults()
default_theme = theme.get_theme()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


# isso é ainda só um placeholder do programa 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configura a window
        self.title(defaults_settings["app_name"] if defaults_settings["app_name"] else "GT5")
        self.geometry(f"{1100}x{580}")
        self.attributes("-zoomed", True) # maximiza o window
        self.background = customtkinter.CTkFrame(self, fg_color=default_theme["ESCURO"])
        self.background.pack(fill="both")


# o programa só roda se for rodado diretamente
if __name__ == "__main__":
    app = App()
    app.mainloop()
import customtkinter
from widgets import sidebar
from lib import theme


class BasePage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="transparent", fg_color="transparent")
        # configura a grid
            #columns
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
            #rows
        self.grid_rowconfigure(0, weight=1)
        
        self.sideBar = sidebar.SideBar(self, theme.current_theme["PRINCIPAL"])
        self.sideBar.grid(column=0, row=0, sticky="NSEW")

        self.contentFrame = ContentFrame(self)
        self.contentFrame.grid(column=1, row=0, sticky="NSEW", padx=50, pady=50)


class ContentFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="transparent", fg_color="transparent")
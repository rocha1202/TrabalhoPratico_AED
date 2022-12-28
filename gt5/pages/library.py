import customtkinter
from pages import base
from widgets import search_bar
from lib import theme


class Library(base.BasePage):
    def __init__(self, master):
        super().__init__(master)
        self.contentFrame.search_bar = search_bar.SearchBar(self.contentFrame, fg_color=theme.current_theme["BRANCO"], text_color=theme.current_theme["ESCURO"])
        self.contentFrame.search_bar.pack()

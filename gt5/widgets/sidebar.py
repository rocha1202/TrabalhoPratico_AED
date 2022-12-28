import customtkinter
from widgets import button

class SideBar(customtkinter.CTkFrame):
    def __init__(self, master, color):
        super().__init__(master, fg_color=color, corner_radius=0)
        self.buttonsFrame = ButtonsFrame(self)
        self.buttonsFrame.pack(pady=10, anchor="center", fill="both")


class ButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent", corner_radius=0)
        self.buttons = []
        self.buttons.append(button.Home(self))
        self.buttons.append(button.Plus(self))
        self.buttons.append(button.Library(self))
        self.buttons.append(button.Heart(self))
        self.buttons.append(button.Settings(self))
        self.buttons.append(button.User(self))

        for i in range(len(self.buttons)):
            self.buttons[i].grid(pady=39)

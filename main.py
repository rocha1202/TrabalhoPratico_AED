from customtkinter import *

# Creates the main window for customtkinter
root = CTk()
root.attributes("-zoomed", True) # maximized

def buttonClick():
    with open('test.txt', 'w') as file:
        file.write('The button was clicked.')

button = CTkButton(root, command=buttonClick)
button.pack()

root.mainloop()
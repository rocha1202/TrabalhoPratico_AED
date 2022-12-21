import customtkinter

customtkinter.set_appearance_mode("system") # segue o tema do sistema

# Creates the main window for customtkinter
root = customtkinter.CTk()
root.attributes("-zoomed", True) # maximized

def buttonClick():
    with open('test.txt', 'w') as file:
        file.write('The button was clicked.')

button = customtkinter.CTkButton(root, command=buttonClick)
button.pack()

root.mainloop()
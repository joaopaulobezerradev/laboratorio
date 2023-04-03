from tkinter import *
from user_interface import UserInterface
from user_logic import UserLogic

# Cria janela do Tkinter
root = Tk()
root.geometry("500x500")

# Cria instância das classes UserInterface e UserLogic
ui = UserInterface(root)
logic = UserLogic()

# Vincula o botão de login à função de lógica
ui.login_button.config(command=lambda: logic.login(ui.username_entry.get(), ui.password_entry.get()))

# Inicia o loop principal
root.mainloop()

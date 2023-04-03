from tkinter import *

class UserInterface:
    def __init__(self, master):
        # Cria label e entry para o nome de usuário
        self.username_label = Label(master, text="Usuário")
        self.username_label.pack()
        self.username_entry = Entry(master)
        self.username_entry.pack()

        # Cria label e entry para a senha
        self.password_label = Label(master, text="Senha")
        self.password_label.pack()
        self.password_entry = Entry(master, show="*")
        self.password_entry.pack()

        # Cria botão de login
        self.login_button = Button(master, text="Login")
        self.login_button.pack()

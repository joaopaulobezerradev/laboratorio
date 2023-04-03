''''import tkinter as tk

# Cria janela do Tkinter
root = tk.Tk()
root.geometry("800x600")

frame1 = tk.Frame(master=root, height=50, bg="purple")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=root, height=25, bg="blue")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=root, height=425, bg="white")
frame3.pack(fill=tk.X)

#Dividindo o frame3 em duas colunas
frame3.columnconfigure(0, weight=1)
frame3.columnconfigure(1, weight=1)

#Adicionando widgets para cada coluna
label1 = tk.Label(master=frame3, text="Coluna 1", bg="red")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(master=frame3, text="Coluna 2", bg="green")
label2.grid(row=0, column=1, padx=10, pady=10)

# Inicia o loop principal
root.mainloop()'''

import tkinter as tk
from PIL import ImageTk, Image

# Cria janela do Tkinter
root = tk.Tk()
root.geometry("900x650")

# Cria três frames/dividi a tela em 3 partes
frame1 = tk.Frame(master=root, height=50, bg="purple")
frame1.pack(fill=tk.X, padx=3, pady=3)

image = Image.open("images/example.png")
image = image.resize((100, 60))
photo = ImageTk.PhotoImage(image)
label = tk.Label(master=frame1, image=photo)
label.pack(side='left')

frame2 = tk.Frame(master=root, height=25, bg="blue")
frame2.pack(fill=tk.X, padx=2, pady=2)

# Esse frame será dividido em 2 colunas
frame3 = tk.Frame(master=root, height=525, bg="white")
frame3.pack(fill=tk.X)

# Dividindo o frame3 em duas colunas
frame3.columnconfigure(0, weight=1)
frame3.columnconfigure(1, weight=1)

# Adicionando widgets para cada coluna
frame_botoes = tk.Frame(master=frame3)
frame_botoes.grid(row=0, column=0, padx=3, pady=(0, 3), sticky="n")

botoes = []
for i in range(11):
    # Adicionando as configurações do botão
    botao = tk.Button(master=frame_botoes, text="Botão " + str(i+1),
                      bg="pink", width=22, height=2, command=lambda i=i: print("Botão", i+1, "clicado!"))
    botoes.append(botao)

for i, botao in enumerate(botoes):
    botao.grid(row=i, column=0, padx=3, pady=3)

label2 = tk.Label(master=frame3, text="Coluna 2",
                  bg="green", width=100, height=34)
label2.grid(row=0, column=1, padx=3, pady=3)


# Inicia o loop principal
root.mainloop()

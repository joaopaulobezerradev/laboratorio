import tkinter as tk
from PIL import ImageTk, Image

# Cria janela do Tkinter
root = tk.Tk()
root.geometry("1000x700")

# Cria três frames/dividi a tela em 3 partes
frame1 = tk.Frame(master=root, height=50, bg="white")
frame1.pack(fill=tk.X, padx=3, pady=3)

image = Image.open("images/example.png")
image = image.resize((160, 60))
photo = ImageTk.PhotoImage(image)
label = tk.Label(master=frame1, image=photo)
label.pack(side='left')

frame2 = tk.Frame(master=root, height=25, bg="white")
frame2.pack(fill=tk.X, padx=2, pady=2)

# Adicionando um botão para recolher a coluna 0 do frame3


def toggle_coluna():
    if frame_botoes.winfo_ismapped():
        frame_botoes.grid_forget()
        frame_botoes.grid_columnconfigure(1, weight=1)
    else:
        frame_botoes.grid(row=0, column=0, padx=3,
                          pady=(0, 3), sticky="n")


botao_toggle = tk.Button(master=frame2, text="MENU",
                         bg="blue", fg="white", command=toggle_coluna, width=21, height=2)
botao_toggle.pack(side=tk.LEFT, padx=3, pady=2)


# Esse frame será dividido em 2 colunas
frame3 = tk.Frame(master=root, height=725, bg="white")
frame3.pack(fill=tk.X)

# Dividindo o frame3 em duas colunas
frame3.columnconfigure(0, weight=1)
frame3.columnconfigure(1, weight=1)

# Adicionando widgets para cada coluna
frame_botoes = tk.Frame(master=frame3)
frame_botoes.grid(row=0, column=0, padx=3, pady=(0, 3), sticky="n")

botoes = []
for i in range(8):
    # Adicionando as configurações do botão
    botao = tk.Button(master=frame_botoes, text="Botão " + str(i+1),
                      bg="pink", width=22, height=2,
                      command=lambda i=i: print("Botão", i+1, "clicado!"))
    botoes.append(botao)

for i, botao in enumerate(botoes):
    botao.grid(row=i, column=0, padx=3, pady=3)

label2 = tk.Label(master=frame3, text="Coluna 2",
                  bg="green", width=120, height=35)
label2.grid(row=0, column=1, padx=3, pady=(0, 3))

# Inicia o loop principal
root.mainloop()

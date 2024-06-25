from main.publishers.publisher import Publisher
import time
import tkinter as tk
from tkinter import ttk

client = Publisher()

def solicitar_arquivo():
    tipo = tipo_arquivo_var.get()
    nome = nome_arquivo.get()
    extensao = extensao_arquivo.get()
    client.sendToRequestFileTopic(f"{tipo}/{nome}/{extensao}")

def disponibilizar_arquivo():
    tipo = tipo_arquivo_var.get()
    nome = nome_arquivo.get()
    extensao = extensao_arquivo.get()
    client.sendToUploadFileTopic(f"{tipo}/{nome}/{extensao}")

# Criação da janela principal
root = tk.Tk()
root.title("MQTTorrent")

# StringVar para o tipo do arquivo
tipo_arquivo_var = tk.StringVar()

# Label e Dropdown list para o tipo do arquivo
tk.Label(root, text="Tipo do arquivo:").grid(row=0, column=0, padx=10, pady=5)
tipo_arquivo = ttk.Combobox(root, textvariable=tipo_arquivo_var, values=["filme", "animacao", "desenho", "logomarca"])
tipo_arquivo.grid(row=0, column=1, padx=10, pady=5)

# Label e Entry para o nome do arquivo
tk.Label(root, text="Nome do arquivo:").grid(row=1, column=0, padx=10, pady=5)
nome_arquivo = tk.Entry(root)
nome_arquivo.grid(row=1, column=1, padx=10, pady=5)

# Label e Entry para a extensão do arquivo
tk.Label(root, text="Extensão do arquivo:").grid(row=2, column=0, padx=10, pady=5)
extensao_arquivo = tk.Entry(root)
extensao_arquivo.grid(row=2, column=1, padx=10, pady=5)

# Botão para solicitar arquivo
btn_solicitar = tk.Button(root, text="Solicitar arquivo", command=lambda: client.sendToRequestFileTopic(tipo_arquivo_var.get() + "/" + nome_arquivo.get() + "/" + extensao_arquivo.get()))
btn_solicitar.grid(row=3, column=0, padx=10, pady=10)

# Botão para disponibilizar arquivo
btn_disponibilizar = tk.Button(root, text="Disponibilizar arquivo", command=lambda: client.sendToUploadFileTopic(tipo_arquivo_var.get() + "/" + nome_arquivo.get() + "/" + extensao_arquivo.get()))
btn_disponibilizar.grid(row=3, column=1, padx=10, pady=10)

# Executa a aplicação
root.mainloop()

# Vamo tentar fazer isso mamnhã.

import tkinter as tk

AUTURA, LARGURA = 700, 600

cores = [
    "#0de5a8",  # cor do texto PRONTO
    "#506ee5"   # cor do texto PREPARANDO
]

# Exemplo de itens
itens_preparando = ["Pedido #101", "Pedido #102", "Pedido #103", *[f"Pedido #{i}" for i in range(104, 160)]]
itens_pronto = ["Pedido #095", "Pedido #096"]

# Criar janela principal
janela = tk.Tk()
janela.geometry(f"{AUTURA}x{LARGURA}")
janela.title("Pedidos")
janela.configure(bg="white")

# Frame principal com 3 colunas
frame_principal = tk.Frame(janela, bg="white")
frame_principal.pack(pady=20)

# ---------- COLUNA 1: PREPARANDO ----------
frame_preparando = tk.Frame(frame_principal, bg="white")
frame_preparando.grid(row=0, column=0, padx=40)

# Rótulo "PREPARANDO:"
rotulo_preparando = tk.Label(frame_preparando, text="PREPARANDO:", font=("Arial", 30, "bold"), fg=cores[1], bg="white")
rotulo_preparando.pack()

# Frame para Listbox + Scrollbar
frame_lista_preparando = tk.Frame(frame_preparando, bg="white")
frame_lista_preparando.pack(pady=10)

# Scrollbar vertical para preparando
scroll_preparando = tk.Scrollbar(frame_lista_preparando, orient=tk.VERTICAL)
scroll_preparando.pack(side=tk.RIGHT, fill=tk.Y)

# Lista de pedidos em preparo com scrollbar
lista_preparando = tk.Listbox(
    frame_lista_preparando,
    width=20,
    height=15,
    font=("Arial", 20),
    fg=cores[1],
    borderwidth=0,
    highlightthickness=0,
    yscrollcommand=scroll_preparando.set
)
lista_preparando.pack(side=tk.LEFT)

scroll_preparando.config(command=lista_preparando.yview)

for item in itens_preparando:
    lista_preparando.insert(tk.END, item)

# ---------- COLUNA 2: PRONTO ----------
frame_pronto = tk.Frame(frame_principal, bg="white")
frame_pronto.grid(row=0, column=2, padx=40)

# Rótulo "PRONTO:"
rotulo_pronto = tk.Label(frame_pronto, text="PRONTO:", font=("Arial", 30, "bold"), fg=cores[0], bg="white")
rotulo_pronto.pack()

# Frame para Listbox + Scrollbar
frame_lista_pronto = tk.Frame(frame_pronto, bg="white")
frame_lista_pronto.pack(pady=10)

# Scrollbar vertical para pronto
scroll_pronto = tk.Scrollbar(frame_lista_pronto, orient=tk.VERTICAL)
scroll_pronto.pack(side=tk.RIGHT, fill=tk.Y)

# Lista de pedidos prontos com scrollbar
lista_pronto = tk.Listbox(
    frame_lista_pronto,
    width=20,
    height=15,
    font=("Arial", 20),
    fg=cores[0],
    borderwidth=0,
    highlightthickness=0,
    yscrollcommand=scroll_pronto.set
)
lista_pronto.pack(side=tk.LEFT)

scroll_pronto.config(command=lista_pronto.yview)

for item in itens_pronto:
    lista_pronto.insert(tk.END, item)

# Iniciar a janela
janela.mainloop()

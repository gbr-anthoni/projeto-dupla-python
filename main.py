import tkinter as tk

# ================= Definição de Configurações e Variáveis Globais =================

# Definir as dimensões das janelas:
AUTURA, LARGURA = 700, 600 # para visualização
AUTURA2,LARGURA2 = 600,500 # para edição

cores = ["#0de5a8", "#506ee5"]  # PRONTO, PREPARANDO

# Dados globais :
itens_preparando = [] # pedidos que estão em preparação
itens_pronto = [] # pedidos que já estão prontos

# Função criar_janela_visualizacao()

def criar_janela_visualizacao():
    janela = tk.Tk()
    janela.geometry(f"{AUTURA}x{LARGURA}")
    janela.title("Pedidos - Visualização")
    janela.configure(bg="white")

    frame_principal = tk.Frame(janela, bg="white")
    frame_principal.pack(pady=20)

    def criar_coluna(titulo, cor, col):
        frame = tk.Frame(frame_principal, bg="white")
        frame.grid(row=0, column=col, padx=40)
        tk.Label(frame, text=titulo, font=("Arial", 30, "bold"), fg=cor, bg="white").pack()

        scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        lista = tk.Listbox(
            frame, width=20, height=15, font=("Arial", 20), fg=cor,
            borderwidth=0, highlightthickness=0, yscrollcommand=scroll.set
        )
        lista.pack(side=tk.LEFT)
        scroll.config(command=lista.yview)
        return lista

    lista_preparando = criar_coluna("PREPARANDO", cores[1], 0)
    lista_pronto = criar_coluna("PRONTO", cores[0], 2)

    def atualizar_listas():
        lista_preparando.delete(0, tk.END)
        lista_pronto.delete(0, tk.END)
        for item in itens_preparando:
            lista_preparando.insert(tk.END, item)
        for item in itens_pronto:
            lista_pronto.insert(tk.END, item)

    def atualizar_periodico():
        atualizar_listas()
        janela.after(500, atualizar_periodico)

    atualizar_periodico()
    return janela

def criar_janela_edicao():
    edicao = tk.Toplevel()
    edicao.geometry(f"{AUTURA2}x{LARGURA2}")
    edicao.title("Editar Pedidos")
    edicao.configure(bg="white")

    tk.Label(edicao, text="Adicionar pedido ao PREPARANDO", font=("Arial", 14, "bold"), bg="white").pack(pady=8)
    entrada_pedido = tk.Entry(edicao, font=("Arial", 12), width=30)
    entrada_pedido.pack(pady=5)

    frame_listas = tk.Frame(edicao, bg="white")
    frame_listas.pack(pady=10)

    def criar_lista(frame, titulo, cor):
        f = tk.Frame(frame, bg="white")
        f.pack(side=tk.LEFT, padx=20)
        tk.Label(f, text=titulo, font=("Arial", 14, "bold"), fg=cor, bg="white").pack()
        lista = tk.Listbox(f, width=25, height=10, font=("Arial", 12), fg=cor)
        lista.pack()
        return lista

    lista_preparando_ed = criar_lista(frame_listas, "PREPARANDO", cores[1])
    lista_pronto_ed = criar_lista(frame_listas, "PRONTO", cores[0])

    def atualizar_listas_edicao():
        lista_preparando_ed.delete(0, tk.END)
        for item in itens_preparando:
            lista_preparando_ed.insert(tk.END, item)

        lista_pronto_ed.delete(0, tk.END)
        for item in itens_pronto:
            lista_pronto_ed.insert(tk.END, item)

    def adicionar_pedido():
        pedido = entrada_pedido.get().strip()
        if pedido and pedido not in itens_preparando and pedido not in itens_pronto:
            itens_preparando.append(pedido)
            entrada_pedido.delete(0, tk.END)
            atualizar_listas_edicao()

    def mover_para_pronto():
        selecionados = lista_preparando_ed.curselection()
        for i in reversed(selecionados):
            itens_pronto.append(itens_preparando.pop(i))
        atualizar_listas_edicao()

    def remover_de_pronto():
        selecionados = lista_pronto_ed.curselection()
        for i in reversed(selecionados):
            itens_pronto.pop(i)
        atualizar_listas_edicao()

    tk.Button(edicao, text="Adicionar", font=("Arial", 12), command=adicionar_pedido).pack(pady=8)
    tk.Button(edicao, text="Mover para PRONTO →", font=("Arial", 12), command=mover_para_pronto).pack(pady=6)
    tk.Button(edicao, text="← Remover de PRONTO", font=("Arial", 12), command=remover_de_pronto).pack(pady=4)

    atualizar_listas_edicao()

    return edicao

if __name__ == "__main__":
    janela_visual = criar_janela_visualizacao()
    janela_edicao = criar_janela_edicao()
    janela_visual.mainloop()
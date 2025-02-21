import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Função para inserir um produto no banco de dados
def inserir_produto():
    codigo = entry_codigo.get()
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()
    data_entrada = entry_data_entrada.get()
    data_validade = entry_data_validade.get()

    # Validação dos campos
    if not (codigo and nome and quantidade and preco and data_entrada and data_validade):
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    # Conectando ao banco de dados
    conn = sqlite3.connect('estoque_laboratorio.db')
    cursor = conn.cursor()

    # Inserindo os dados do produto
    cursor.execute("""
    INSERT INTO estoque (codigo_produto, nome_produto, quantidade_estoque, preco_unitario, data_entrada, data_validade)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (codigo, nome, int(quantidade), float(preco), data_entrada, data_validade))

    # Salvando e fechando
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")
    limpar_campos()

# Função para visualizar todos os produtos no banco de dados
def visualizar_produtos():
    # Conectando ao banco de dados
    conn = sqlite3.connect('estoque_laboratorio.db')
    cursor = conn.cursor()

    # Consultando todos os produtos
    cursor.execute("SELECT * FROM estoque")
    produtos = cursor.fetchall()

    # Fechando a conexão
    conn.close()

    # Limpando a tela de resultados
    listbox_produtos.delete(0, tk.END)

    # Exibindo os produtos na listbox
    for produto in produtos:
        listbox_produtos.insert(tk.END, f"Código: {produto[1]}, Nome: {produto[2]}, Qtd: {produto[3]}, Preço: {produto[4]}, Entrada: {produto[5]}, Validade: {produto[6]}")

# Função para limpar os campos
def limpar_campos():
    entry_codigo.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_data_entrada.delete(0, tk.END)
    entry_data_validade.delete(0, tk.END)

# Criando a janela principal
root = tk.Tk()
root.title("Controle de Estoque - Laboratório")
root.geometry("600x400")

# Labels e campos de entrada
tk.Label(root, text="Código do Produto:").pack(pady=5)
entry_codigo = tk.Entry(root)
entry_codigo.pack(pady=5)

tk.Label(root, text="Nome do Produto:").pack(pady=5)
entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

tk.Label(root, text="Quantidade em Estoque:").pack(pady=5)
entry_quantidade = tk.Entry(root)
entry_quantidade.pack(pady=5)

tk.Label(root, text="Preço Unitário:").pack(pady=5)
entry_preco = tk.Entry(root)
entry_preco.pack(pady=5)

tk.Label(root, text="Data de Entrada (YYYY-MM-DD):").pack(pady=5)
entry_data_entrada = tk.Entry(root)
entry_data_entrada.pack(pady=5)

tk.Label(root, text="Data de Validade (YYYY-MM-DD):").pack(pady=5)
entry_data_validade = tk.Entry(root)
entry_data_validade.pack(pady=5)

# Botões
button_inserir = tk.Button(root, text="Inserir Produto", command=inserir_produto)
button_inserir.pack(pady=10)

button_visualizar = tk.Button(root, text="Visualizar Produtos", command=visualizar_produtos)
button_visualizar.pack(pady=10)

# Lista de produtos
listbox_produtos = tk.Listbox(root, width=80, height=10)
listbox_produtos.pack(pady=10)

# Rodando a interface gráfica
root.mainloop()

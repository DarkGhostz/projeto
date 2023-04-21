import mysql.connector
import os
import tkinter as tk


# Função para postar um novo item com nome e preço no banco de dados
def postar_novo_item():
    nome = entry_nome.get()
    preco = float(entry_preco.get())
    query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
    cursor.execute(query, (nome, preco))
    cnx.commit()
    lbl_mensagem.config(text="Novo item postado com sucesso")

    


# Função para deletar um item do banco de dados
def deletar_item():
    id = entry_id_produto.get()
    query = "DELETE FROM produtos WHERE id = %s"
    cursor.execute(query, (id,))
    cnx.commit()
    lbl_mensagem.config(text=f"Item com ID {id} deletado com sucesso")


# Resto do código

# Conexão ao banco de dados MySQL
cnx = mysql.connector.connect(
    host="localhost",
    user=os.getenv('user'),
    password=os.getenv('senha'),
    database=os.getenv('database')
)
cursor = cnx.cursor()

# Criação dos widgets do Tkinter
root = tk.Tk()
root.title("Adicionar itens")
root.geometry("828x1792")




# Widget para entrada do nome do item
label_nome = tk.Label(root, text="Nome do Produto:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

# Widget para entrada do preço do item
label_preco = tk.Label(root, text="Preço do Produto:")
entry_preco = tk.Entry(root)
label_preco.pack()
entry_preco.pack()

# Botão para postar um novo item
btn_postar = tk.Button(root, text="Postar Novo Item", command=postar_novo_item)
btn_postar.pack()

# Widget para entrada do ID do item a ser deletado
entry_id_produto = tk.Entry(root)
entry_id_produto.pack()

# Botão para deletar um item
btn_deletar = tk.Button(root, text="Deletar Item", command=deletar_item)
btn_deletar.pack()

# Label para exibir mensagens de status
lbl_mensagem = tk.Label(root)
lbl_mensagem.pack()

# Resto do código

root.mainloop()

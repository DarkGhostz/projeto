import mysql.connector
import os
import tkinter as tk

# Função para calcular o valor total com base na quantidade de produtos
def calcular_valor_total():
    id = entry_id_NM.get()
    id = entry_id.get().split(',') # IDs separados por vírgulas
    quantidades = entry_quantidade.get().split(',') # Quantidades separadas por vírgulas
    valor_total = 0
    for id, quantidade in zip(id, quantidades):
        id = int(id.strip()) # Converte o ID para inteiro e remove espaços em branco
        quantidade = int(quantidade.strip()) # Converte a quantidade para inteiro e remove espaços em branco
        # Consulta para obter o preço do produto pelo ID
        query = "SELECT preco FROM produtos WHERE id = %s"
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        if row is not None:
            preco = row[0]
            valor_total += preco * quantidade  # Multiplica o preço pela quantidade
        else:
            lbl_valor_total.config(text="Produto não encontrado")
            return
    lbl_valor_total.config(text=f"Valor total: R${valor_total:.2f}")


# Função para fechar a conexão com o banco de dados
def fechar_conexao():
    cursor.close()
    cnx.close()
    root.destroy()



# Conexão ao banco de dados MySQL
cnx = mysql.connector.connect(
    host="localhost",
    user=os.getenv('user'),
    password=os.getenv('senha'),
    database=os.getenv('database')
)
cursor = cnx.cursor()

# Configurações da janela do Tkinter
root = tk.Tk()
root.title("Exemplo de Cálculo de Valor Total")
root.geometry("828x1792")

# Widgets do Tkinter
lbl_id_NM = tk.Label(root, text="Nome ou Mesa:")
lbl_id_NM.pack()
entry_id_NM = tk.Entry(root)
entry_id_NM.pack()


lbl_id = tk.Label(root, text="ID:")
lbl_id.pack()
entry_id = tk.Entry(root)
entry_id.pack()

lbl_quantidade = tk.Label(root, text="Quantidade:")
lbl_quantidade.pack()
entry_quantidade = tk.Entry(root)
entry_quantidade.pack()

btn_calcular = tk.Button(root, text="Calcular", command=calcular_valor_total)
btn_calcular.pack()

lbl_valor_total = tk.Label(root, text="")
lbl_valor_total.pack()

btn_fechar = tk.Button(root, text="Fechar", command=fechar_conexao)
btn_fechar.pack()

texto = "ID:\n1- Assado\n2- Coxinha"
lbl = tk.Label(root, text=texto)
lbl.pack()

root.mainloop()



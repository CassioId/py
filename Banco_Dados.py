import sqlite3

# Conectando ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect('estoque_laboratorio.db')
cursor = conn.cursor()

# Criando a tabela (se não existir)
cursor.execute("""
CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_produto TEXT NOT NULL,
    nome_produto TEXT NOT NULL,
    quantidade_estoque INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    data_entrada TEXT,
    data_validade TEXT
)
""")

# Salvando e fechando
conn.commit()
conn.close()

print("Banco de dados e tabela criados com sucesso!")

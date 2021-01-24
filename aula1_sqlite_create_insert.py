import sqlite3


# cria banco de dados
banco = sqlite3.connect('primeiro_banco.sqlite3')


# cria operador do banco de dados
cursor = banco.cursor()

# cria tabela
# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

# inseri dados na tabela
cursor.execute("INSERT INTO pessoas VALUES ('Marcos', '40', 'maroberto13@gmail.com')")

# executa a insersão
banco.commit()

# mostra dados do banco
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())

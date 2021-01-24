import sqlite3

nome = 'Junior'
idade = 28
email = 'junior@gmail.com'

# cria banco de dados
banco = sqlite3.connect('primeiro_banco.sqlite3')


# cria operador do banco de dados
cursor = banco.cursor()

# cria tabela
# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

# inseri dados na tabela
#cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"', "+str(40)+", '"+email+"')")

# atualizar tabela
cursor.execute("UPDATE pessoas SET nome = 'Carlos' WHERE idade = 40")

# executa a insersão
banco.commit()

# mostra dados do banco
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())

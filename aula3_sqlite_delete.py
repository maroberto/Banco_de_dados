import sqlite3

try:
    # cria banco de dados
    banco = sqlite3.connect('primeiro_banco.sqlite3')

    # cria operador do banco de dados
    cursor = banco.cursor()

    # cria tabela
    # cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

    # inseri dados na tabela
    cursor.execute("DELETE from pessoas WHERE idade = 40")

    # executa a insersão
    banco.commit()
    banco.close()
    print('Os dados foram removidos com sucesso!')
except sqlite3.Error as erro:
    print('Erro ao excluir: ', erro)

# mostra dados do banco
# cursor.execute("SELECT * FROM pessoas")
# print(cursor.fetchall())

import sqlite3

class UserLogic:
    def __init__(self):
        # Conecta ao banco de dados
        self.conn = sqlite3.connect('lab.db')

    def login(self, username, password):
        # Cria objeto cursor
        cursor = self.conn.cursor()

        # Executa consulta SQL para recuperar informações do usuário
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

        # Recupera resultados e verifica se o usuário existe
        result = cursor.fetchone()
        if result:
            # Usuário existe - faça algo aqui
            print("Usuário existe!")
        else:
            # Usuário não existe - faça algo aqui
            print("Usuário não existe!")

    def __del__(self):
        # Fecha a conexão e confirma as alterações
        self.conn.commit()
        self.conn.close()
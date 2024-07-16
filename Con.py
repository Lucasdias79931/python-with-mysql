import mysql.connector

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão ao MySQL bem-sucedida!")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao MySQL: {err}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexão ao MySQL fechada.")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return None
        finally:
            cursor.close()




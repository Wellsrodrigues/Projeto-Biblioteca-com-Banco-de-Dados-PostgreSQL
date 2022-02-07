import psycopg2


class DataBase():
    def __init__(self):
        self.banco = None

    def conectar(self):
        banco = psycopg2.connect(
            host = "localhost",
            database = "Biblioteca",
            user = "postgres",
            password = "12345"
        )
        return banco

    def desconectar(self):
        self.banco.close()

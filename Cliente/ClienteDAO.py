from Connection.DataBase import DataBase


class ClienteDAO:

    def __init__(self):
        pass

    def insert(self, cliente):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        script = "insert into cliente (nome, cpf, telefone) values ('" + cliente.getNome() + "', '" + cliente.getCpf() + "', '" + cliente.getTelefone() + "')"
        cursor.execute(script)
        bd.commit()

    def select(self, cod):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from cliente where id = " + cod)
        resultado = cursor.fetchone()
        return resultado

    def selectAll(self):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from cliente  order by id")
        resultado = cursor.fetchall()
        return resultado

    def delete(self, cod):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("delete from cliente where id =" + cod)
        bd.commit()

    def update(self, cod, campo, valor):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("update cliente set {} = '{}' where id = {}".format(campo, valor, cod))
        bd.commit()

    def dropTable(self):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("delete from cliente")
        bd.commit()

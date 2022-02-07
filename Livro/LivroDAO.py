from Connection.DataBase import DataBase


class LivroDAO:

    def __init__(self):
        pass

    def insert(self, livro):
        bd  = DataBase().conectar()
        cursor = bd.cursor()
        script = "insert into livro (titulo, author, estado, disponibilidade) values ('"+livro.getTitulo()+"', '"+livro.getAuthor()+"', '"+livro.getEstado()+"', '"+livro.getDisponibilidade()+"')"
        cursor.execute(script)
        bd.commit()

    def select(self, cod):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from livro where cod = "+cod)
        resultado = cursor.fetchone()
        return resultado

    def selectAll(self):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from livro order by cod")
        resultado = cursor.fetchall()
        return resultado

    def delete(self, cod):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("delete from livro where cod="+cod)
        bd.commit()
        

    def update(self, cod, campo, valor):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("update livro set {} = '{}' where cod = {}" .format(campo, valor, cod))
        bd.commit()

    def dropTable(self):
        bd = DataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("delete from livro")
        bd.commit()

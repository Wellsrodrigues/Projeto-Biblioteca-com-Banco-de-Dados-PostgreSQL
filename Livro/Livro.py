from Livro.LivroDAO import LivroDAO

class Livro:

    def __init__(self):
        pass

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getAuthor(self):
        return self.author

    def setAuthor(self, author):
        self.author = author

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getDisponibilidade(self):
        return  self.disponibilidade

    def setDisponibilidade(self, disponibilidade):
        self.disponibilidade = disponibilidade


    def cadastrarLivro(sefl, titulo, author, estado, disponibilidade):
        livro = Livro()

        livro.setTitulo(titulo)
        livro.setAuthor(author)
        livro.setEstado(estado)
        livro.setDisponibilidade(disponibilidade)

        dao = LivroDAO()
        dao.insert(livro)

    def exibirLivros(sefl):
        dao = LivroDAO()
        resultado = dao.selectAll()
        return (resultado)


    def buscarLivro(self, cod):
        dao = LivroDAO()
        resultado = dao.select(cod)
        return (resultado)


    def deletarLivro(self, cod):
        dao = LivroDAO()
        dao.delete(cod)

    def atualizarLivro(sefl, cod, campo, valor):
        dao = LivroDAO()
        dao.update(cod, campo, valor)

    def deletarTodos(self):
        dao = LivroDAO()
        dao.dropTable()



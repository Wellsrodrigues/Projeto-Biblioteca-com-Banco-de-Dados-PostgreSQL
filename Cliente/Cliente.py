from Cliente.ClienteDAO import ClienteDAO

class Cliente:

    def __init__(self):
        pass

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome;

    def getCpf(self):
        return self.cpf
    
    def setCpf(self, cpf):
        self.cpf = cpf

    def getTelefone(self):
        return self.telefone
    
    def setTelefone(self, telefone):
        self.telefone = telefone

    def cadastrarCliente(sefl, nome, cpf, telefone):
        cliente = Cliente()
        cliente.setNome(nome)
        cliente.setCpf(cpf)
        cliente.setTelefone(telefone)
        
        dao = ClienteDAO()
        dao.insert(cliente)

    def exibirClientes(sefl):
        dao = ClienteDAO()
        resultado = dao.selectAll()
        return resultado

    def buscarCliente(sefl, cod):
        dao = ClienteDAO()
        resultado = dao.select(cod)
        return resultado


    def deletarCliente(self, cod):
        dao = ClienteDAO()
        dao.delete(cod)

    def atualizarCliente(sefl, cod, campo, valor):
        dao = ClienteDAO()
        dao.update(cod, campo, valor)
        
    def deletarTodos(self):
        dao = ClienteDAO()
        dao.dropTable()

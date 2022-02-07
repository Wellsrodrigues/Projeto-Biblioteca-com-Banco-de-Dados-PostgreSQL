import tkinter as tk
from Cliente.Cliente import Cliente
from tkinter import messagebox

cliente = Cliente()

class TelaCliente:
    def __init__(self, master):
        self.nova = master
        self.nova.title("Cliente")

        self.frame1 = tk.Frame(self.nova, background="#87CEEB")
        self.frame1.place(x=30, y=50, width=750, height=200)

        self.id = tk.Label(self.frame1, text="ID: ", bg="#87CEEB", font=("Verdana", "18", "bold"))
        self.id.place(x=20, y=50)

        self.entrada0 = tk.Entry(self.frame1, font=("verdana", "15", "bold") ,width=15, border=5)
        self.entrada0.place(x=20, y=100)

        self.bot1 = tk.Button(self.frame1, text="Buscar", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
                             command=self.buscar)
        self.bot1.place(x=300, y=80)

        self.bot2 = tk.Button(self.frame1, text="Alterar", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
                              command=self.alterar)
        self.bot2.place(x=450, y=80)

        self.bot3 = tk.Button(self.frame1, text="Excluir", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
                              command=self.excluir)
        self.bot3.place(x=600, y=80)


        self.frame2 = tk.Frame(self.nova, background="#87CEEB")
        self.frame2.place(x=30, y=300, width=750, height=380)

        self.nome = tk.Label(self.frame2, text="NOME: ", bg="#87CEEB", font=("Verdana","18","bold"))
        self.nome.place(x=20, y=50)

        self.entrada = tk.Entry(self.frame2, width=50, border=5, font=("verdana", "15", "bold"))
        self.entrada.place(x=20, y=100)

        self.text2 = tk.Label(self.frame2, text="CPF: ", bg="#87CEEB", font=("Verdana","18","bold"))
        self.text2.place(x=20, y=180)

        self.entrada2 = tk.Entry(self.frame2, width=20, border=5, font=("verdana", "15", "bold"))
        self.entrada2.place(x=20, y=230)

        self.text3 = tk.Label(self.frame2, text="TELEFONE: ", bg="#87CEEB", width=10, font=("Verdana","18","bold"))
        self.text3.place(x=450, y=180)

        self.entrada3 = tk.Entry(self.frame2, width=19, border=5, font=("verdana", "15", "bold"))
        self.entrada3.place(x=450, y=230)

        self.bot4 = tk.Button(self.frame2, text="Cadastrar", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5, command=self.cadastrar)
        self.bot4.place(x=180, y=300)

        self.bot4 = tk.Button(self.frame2, text="Limpar", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5, width=8, command=self.limpar)
        self.bot4.place(x=450, y=300)

        self.frame3 = tk.Frame(self.nova, background="#87CEEB")
        self.frame3.place(x=800, y=50, width=530, height=630)

        self.tex4 = tk.Label(self.frame3, text="Banco de Dados", font=("Verdana", "18", "bold"), background="#87CEEB")
        self.tex4.place(x=130, y=20)

        self.frame4 = tk.Frame(self.frame3, background="white")
        self.frame4.place(x=20, y=80, width=485, height=520)

        self.text5 = tk.Label(self.frame4, text="  ID      NOME\t      CPF\t\tTELEFONE", font=("verdana", "12", "bold"), background="white")
        self.text5.place(x=20, y=10)

        self.linha = tk.Label(self.frame4,
        text="------------------------------------------------------------------------------------------------",
        background="white", font=("", "12", "bold"))
        self.linha.place(x=0, y=30)


        self.bot5 = tk.Button(self.frame4, text="Listar Dados", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5, command=self.exibir)
        self.bot5.place(x=50, y=450)

        self.bot6 = tk.Button(self.frame4, text="Limpar Tela", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5, command=self.limparTela)
        self.bot6.place(x=250, y=450)

        self.frame5 = tk.Frame(self.frame4, background="white")
        self.frame5.place(x=0, y=50, width=500, height=400)

        self.nova.geometry('1366x768+-10+0')
        self.nova.configure(background="#20B2AA")
        #self.nova.resizable(False, False)
        self.nova.focus_force()
        self.nova.grab_set()

    def verificarId(self):
        resultado = cliente.buscarCliente(self.entrada0.get())
        if(resultado == None):
            messagebox.showerror("Erro", "O Id informado não foi encontrado!")
            return False
        else:
            return True

    def idVazio(self):
        if (self.entrada0.get() == ""):
            messagebox.showwarning("Aviso", "Insira um Id para continuar!")
            return True
        else:
            return False

    def baseDados(self):
        resultado = cliente.exibirClientes()
        if (len(resultado) == 0):
            self.frame5.destroy()
            messagebox.showwarning("Aviso", "Não há informações na Base de Dados!")
            return False
        else:
            return True

    def limpar(self):
        self.entrada.delete(0, 'end')
        self.entrada2.delete(0, 'end')
        self.entrada3.delete(0, 'end')


    def cadastrar(self):
        self.entrada.bind("<Button-1>")
        self.entrada2.bind("<Button-1>")
        self.entrada3.bind("<Button-1>")

        if (self.entrada.get() == "" and self.entrada2.get() == "" and self.entrada3.get() == ""):
            messagebox.showwarning("Aviso", "Campos Vazios!")
        else:
            insere = cliente.cadastrarCliente(self.entrada.get(), self.entrada2.get(), self.entrada3.get())
            self.exibir()

    def buscar(self):
        self.entrada0.bind("<Button-1>")
        if (self.baseDados() == True):
            if (self.idVazio() == False):
                resultado = cliente.buscarCliente(self.entrada0.get())

                if(self.verificarId() == True):
                    messagebox.showinfo("Cliente Encontrado","Nome: {}\n\nCpf: {}\n\nTelefone: {}".format(resultado[1], resultado[2], resultado[3]))

    def excluir(self):
        self.entrada0.bind("<Button-1>")
        if (self.baseDados() == True):
            if (self.idVazio() == False):
                opp = messagebox.askyesnocancel("Excluir Dados", "Você tem certeza?")
                if (opp == True):
                    if (self.verificarId() == True):
                        cliente.deletarCliente(self.entrada0.get())
                        self.exibir()

    def alterar(self):
        self.entrada0.bind("<Button-1>")
        self.entrada.bind("<Button-1>")
        self.entrada2.bind("<Button-1>")
        self.entrada3.bind("<Button-1>")

        if (self.baseDados() == True):
            if(self.idVazio() == False):
                if (self.verificarId() == True):
                    if(self.entrada.get() != ""):
                        cliente.atualizarCliente(self.entrada0.get(), "nome", self.entrada.get())
                    if(self.entrada2.get() != ""):
                        cliente.atualizarCliente(self.entrada0.get(), "cpf", self.entrada2.get())
                    if(self.entrada3.get() != ""):
                        cliente.atualizarCliente(self.entrada0.get(), "telefone", self.entrada3.get())

                    if(self.entrada.get() == "" and self.entrada2.get() == "" and self.entrada3.get() == ""):
                        messagebox.showwarning("Aviso", "Insira um valor em um dos campos para atualizar")
                    else:
                        self.exibir()

    def exibir(self):
        self.frame5.destroy()

        if(self.baseDados() == True):
            self.frame5 = tk.Frame(self.frame4, background="red")
            self.frame5.place(x=10, y=50, height=380, width=475)

            self.scrollbar = tk.Scrollbar(self.frame5)
            self.scrollbar.pack(side="right", fill="y")
            self.listbox = tk.Listbox(self.frame5, yscrollcommand=self.scrollbar.set)

            texto = tk.Text(self.frame5, font=("Verdana", "12", "italic"))
            texto.pack(expand=True, fill="both", side="left")

            resultado = cliente.exibirClientes()
            lista = [[] for _ in range(len(resultado))]

            for i in range(len(resultado)):
                lista[i].append(resultado[i])

            linha = " ---------------------------------------------------------------- "
            for i in range(len(lista)):
                lbl = "\n  {}\t{}\t{}\t\t{}\n".format(lista[i][0][0], lista[i][0][1], lista[i][0][2], lista[i][0][3])
                texto.insert("end", lbl)
                texto.insert("end", linha)
            texto.config(yscrollcommand=self.scrollbar.set)
            self.scrollbar.config(command=texto.yview)

    def limparTela(self):
        self.frame5.destroy()










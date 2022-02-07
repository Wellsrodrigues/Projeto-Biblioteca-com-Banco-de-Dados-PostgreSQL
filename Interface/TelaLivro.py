import tkinter as tk
from tkinter import messagebox
from Livro.Livro import Livro

livro = Livro()

class TelaLivro:
    def __init__(self, master):
        self.nova = master
        self.nova.title("Livro")

        self.frame1 = tk.Frame(self.nova, background="#87CEEB")
        self.frame1.place(x=20, y=50, width=700, height=150)

        self.id = tk.Label(self.frame1, text="COD: ", bg="#87CEEB", font=("Verdana", "18", "bold"))
        self.id.place(x=20, y=30)

        self.entrada0 = tk.Entry(self.frame1, font=("verdana", "15", "bold"), width=10, border=5)
        self.entrada0.place(x=20, y=80)

        self.bot1 = tk.Button(self.frame1, text="Buscar", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
                              command=self.buscar)
        self.bot1.place(x=250, y=50)

        self.bot2 = tk.Button(self.frame1, text="Alterar", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
                              command=self.alterar)
        self.bot2.place(x=400, y=50)

        self.bot3 = tk.Button(self.frame1, text="Excluir", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
                                command=self.excluir)
        self.bot3.place(x=550, y=50)

        self.frame2 = tk.Frame(self.nova, background="#87CEEB")
        self.frame2.place(x=20, y=230, width=700, height=440)

        self.nome = tk.Label(self.frame2, text="TITULO:", bg="#87CEEB", font=("Verdana", "18", "bold"))
        self.nome.place(x=20, y=50)

        self.entrada = tk.Entry(self.frame2, width=20, border=5, font=("verdana", "15", "bold"))
        self.entrada.place(x=20, y=100)

        self.text2 = tk.Label(self.frame2, text="AUTHOR:", bg="#87CEEB", font=("Verdana", "18", "bold"))
        self.text2.place(x=380, y=50)

        self.entrada2 = tk.Entry(self.frame2, width=20, border=5, font=("verdana", "15", "bold"))
        self.entrada2.place(x=380, y=100)

        self.text3 = tk.Label(self.frame2, text="ESTADO:", bg="#87CEEB", font=("Verdana", "18", "bold"))
        self.text3.place(x=20, y=200)

        self.entrada3 = tk.Entry(self.frame2, width=20, border=5, font=("verdana", "15", "bold"))
        self.entrada3.place(x=20, y=250)

        self.text6 = tk.Label(self.frame2, text="DISPONIBILIDADE:", bg="#87CEEB", font=("Verdana", "18", "bold"))
        self.text6.place(x=380, y=200)

        self.entrada6 = tk.Entry(self.frame2, width=20, border=5, font=("verdana", "15", "bold"))
        self.entrada6.place(x=380, y=250)

        self.bot4 = tk.Button(self.frame2, text="Cadastrar", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
                              command=self.cadastrar)
        self.bot4.place(x=100, y=350)

        self.bot4 = tk.Button(self.frame2, text="Limpar", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5, width=8,
                              command=self.limpar)
        self.bot4.place(x=450, y=350)

        self.frame3 = tk.Frame(self.nova, background="#87CEEB")
        self.frame3.place(x=750, y=50, width=600, height=620)

        self.tex4 = tk.Label(self.frame3, text="Banco de Dados", font=("Verdana", "18", "bold"), background="#87CEEB")
        self.tex4.place(x=200, y=20)

        self.frame4 = tk.Frame(self.frame3, background="white")
        self.frame4.place(x=20, y=80, width=560, height=520)

        self.text5 = tk.Label(self.frame4, text="COD          TITULO            AUTHOR          ESTADO          DISPO.",
        font=("verdana", "12", "bold"), background="white")
        self.text5.place(x=15, y=20)

        self.linha = tk.Label(self.frame4, text="---------------------------------------------------------------------------------------------------------------",
        background="white", font=("", "12", "bold"))
        self.linha.place(x=0, y=40)

        self.bot5 = tk.Button(self.frame4, text="Listar Dados", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
        command=self.exibir)
        self.bot5.place(x=50, y=450)

        self.bot6 = tk.Button(self.frame4, text="limpar Tela", font=("Verdana", "15", "bold"), bg="#4682B4", bd=5,
        command=self.limparTela)
        self.bot6.place(x=330, y=450)

        self.frame5 = tk.Frame(self.frame4, background="white")
        self.frame5.place(x=0, y=58, width=560, height=400)

        self.nova.geometry('1366x768+-10+0')
        self.nova.configure(background="#20B2AA")
        # self.nova.resizable(False, False)
        self.nova.focus_force()
        self.nova.grab_set()

    def verificarCod(self):
        resultado = livro.buscarLivro(self.entrada0.get())
        if (resultado == None):
            messagebox.showerror("Erro", "O cod informado não foi encontrado!")
            return False
        else:
            return True

    def CodVazio(self):
        if (self.entrada0.get() == ""):
            messagebox.showwarning("Aviso", "Insira um cod para continuar!")
            return True
        else:
            return False

    def baseDados(self):
        resultado = livro.exibirLivros()
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
        self.entrada6.delete(0, 'end')

    def cadastrar(self):
        self.entrada.bind("<Button-1>")
        self.entrada2.bind("<Button-1>")
        self.entrada3.bind("<Button-1>")
        self.entrada6.bind("<Button-1>")

        if (self.entrada.get() == "" and self.entrada2.get() == "" and self.entrada3.get() == "" and self.entrada6.get() == ""):
            messagebox.showwarning("Aviso", "Campos Vazios!")
        else:
            insere = livro.cadastrarLivro(self.entrada.get(), self.entrada2.get(), self.entrada3.get(), self.entrada6.get())
            self.exibir()

    def buscar(self):
        self.entrada0.bind("<Button-1>")
        if (self.baseDados() == True):
            if (self.CodVazio() == False):
                resultado = livro.buscarLivro(self.entrada0.get())

                if (self.verificarCod() == True):
                    messagebox.showinfo("Livro Encontrado", "Titulo: {}\n\nAuthor: {}\n\nEstado: {}\n\nDisponibilidade: {}".format(resultado[1], resultado[2],
                                                                                     resultado[3], resultado[4]))

    def excluir(self):
        self.entrada0.bind("<Button-1>")
        if (self.baseDados() == True):
            if (self.CodVazio() == False):
                opp = messagebox.askyesnocancel("Excluir Dados", "Você tem certeza?")
                if (opp == True):
                    if (self.verificarCod() == True):
                        livro.deletarLivro(self.entrada0.get())
                        self.exibir()

    def alterar(self):
        self.entrada0.bind("<Button-1>")
        self.entrada.bind("<Button-1>")
        self.entrada2.bind("<Button-1>")
        self.entrada3.bind("<Button-1>")
        self.entrada6.bind("<Button-1>")

        if (self.baseDados() == True):
            if (self.CodVazio() == False):
                if (self.verificarCod() == True):
                    if (self.entrada.get() != ""):
                        livro.atualizarLivro(self.entrada0.get(), "titulo", self.entrada.get())
                    if (self.entrada2.get() != ""):
                        livro.atualizarLivro(self.entrada0.get(), "author", self.entrada2.get())
                    if (self.entrada3.get() != ""):
                        livro.atualizarLivro(self.entrada0.get(), "estado", self.entrada3.get())
                    if (self.entrada6.get() != ""):
                        livro.atualizarLivro(self.entrada0.get(), "disponibilidade", self.entrada6.get())

                    if (self.entrada.get() == "" and self.entrada2.get() == "" and self.entrada3.get() == "" and self.entrada6.get() == ""):
                        messagebox.showwarning("Aviso", "Insira um valor em um dos campos para atualizar")
                    else:
                        self.exibir()

    def exibir(self):
        self.frame5.destroy()

        if (self.baseDados() == True):
            self.frame5 = tk.Frame(self.frame4, background="red")
            self.frame5.place(x=10, y=70, height=360, width=550)

            self.scrollbar = tk.Scrollbar(self.frame5)
            self.scrollbar.pack(side="right", fill="y")
            self.listbox = tk.Listbox(self.frame5, yscrollcommand=self.scrollbar.set)

            texto = tk.Text(self.frame5, font=("Verdana", "12", "italic"))
            texto.pack(expand=True, fill="both", side="left")

            resultado = livro.exibirLivros()
            lista = [[] for _ in range(len(resultado))]

            for i in range(len(resultado)):
                lista[i].append(resultado[i])

            linha = " -------------------------------------------------------------------------- "
            for i in range(len(lista)):
                lbl = "\n  {}\t  {}\t\t{}\t       {}\t\t{}\n".format(lista[i][0][0], lista[i][0][1], lista[i][0][2], lista[i][0][3], lista[i][0][4])
                texto.insert("end", lbl)
                texto.insert("end", linha)
            texto.config(yscrollcommand=self.scrollbar.set)
            self.scrollbar.config(command=texto.yview)

    def limparTela(self):
        self.frame5.destroy()




        

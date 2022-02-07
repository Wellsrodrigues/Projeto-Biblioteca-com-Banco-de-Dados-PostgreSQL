import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Interface.TelaCliente import TelaCliente
from Interface.TelaLivro import TelaLivro

class TelaPrincipal:
    def __init__(self, master):
        self.Tela = master
        self.Tela.title("Sistema da Biblioteca Pôr do Sol")
        self.Tela.configure(background="#008080")
        self.barraMenu = tk.Menu(self.Tela)
        self.Tela.config(menu = self.barraMenu)

        self.barraMenu.add_cascade(label="Livros", command=self.oppLivro)
        self.barraMenu.add_cascade(label="Cliente", command=self.oppCliente)
        self.barraMenu.add_command(label="Ajuda", command=self.oppAjuda)
        self.barraMenu.add_command(label="Sobre nós", command=self.oppInfo)
        self.barraMenu.add_command(label="Sair", command=self.oppSair)

        image = Image.open("C:/Users/Wells/PycharmProjects/Interface Grafica/venv/Imagens/Fundo.png")
        image = image.resize((1400,700), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(image)
        logo = tk.Label(self.Tela, image=img)
        logo.place(x=0, y=0)

        imagem = tk.PhotoImage(file="C:/Users/Wells/PycharmProjects/Interface Grafica/venv/Imagens/Biblioteca Pôr do Sol.png")
        w = tk.Label(self.Tela, image=imagem)
        w.imagem = imagem
        w.place(x=440, y=150, height=350)

        master.geometry('1366x768+-10+0')
        master.mainloop()

    def oppCliente(self):
        self.novaTela = tk.Toplevel(self.Tela)
        TelaCliente(self.novaTela)

    def oppLivro(self):
        self.novaTela = tk.Toplevel(self.Tela)
        TelaLivro(self.novaTela)

    def oppSair(self):
        opp = messagebox.askquestion("Encerrar Programa", "Tem certeza?")
        if (opp == 'yes'):
            exit()

    def oppAjuda(self):
        self.novaTela = tk.Toplevel(self.Tela)
        self.novaTela.title("Ajuda")
        self.novaTela.config(background="white")

        imagem = tk.PhotoImage(file="C:/Users/Wells/PycharmProjects/Interface Grafica/venv/Imagens/jesus.gif")
        w = tk.Label(self.novaTela, image=imagem)
        w.imagem = imagem
        w.place(x=150, y=50)

        self.novaTela.geometry('510x500+430+100')

    def oppInfo(self):
        self.novaTela = tk.Toplevel(self.Tela)
        self.novaTela.title("Créditos")
        self.novaTela.config(background="#F8F8FF")

        imagem = tk.PhotoImage(file="C:/Users/Wells/PycharmProjects/Interface Grafica/venv/Imagens/image.png")
        w = tk.Label(self.novaTela, image=imagem)
        w.imagem = imagem
        w.place(x=85, y=20)

        tk.Label(self.novaTela,text="  ", bg="#F8F8FF").pack(side=tk.BOTTOM)
        tk.Label(self.novaTela, text="Orientador: Prof. Anderson Costa", bg="#F8F8FF",
        font=("Verdana", "18", "bold italic")).pack(side=tk.BOTTOM)
        tk.Label(self.novaTela, text="Author: Wellison Rodrigues", bg="#F8F8FF", font=("Verdana","18","bold italic")).pack(side=tk.BOTTOM)

        self.novaTela.geometry('510x500+430+100')









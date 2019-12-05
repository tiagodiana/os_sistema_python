from tkinter import *


from CadastroCliente import CadastroCliente
from BuscarCliente import BuscarCliente

from tkinter import messagebox


class Inicio():
    def __init__(self, master):
        font = ('arial', 14, 'bold')
        self.form = master
        self.form.geometry('800x500+300+150')
        self.form.title("Sistema de OS")
        self.form.config(background="dodgerblue")
        self.lbl1 = Label(text='Sistema de Ordem de Serviço', font=('Times New Roman', 18, 'bold'), bg='#204961', fg='white')
        self.lbl1.pack(anchor=N, fill=X, ipady=15)

        self.img = PhotoImage(file='image/logo-icone.png')
        self.lblimg = Label(self.form, image=self.img, bg='dodgerblue')
        self.lblimg.place(x=290, y=290)

        # BOTÕES CLIENTE
        self.btn1 = Button(text='Cadastro de Cliente', font=font, width=23, height=2, bg='#204961', fg='white',
                           activebackground='#468AE8', command=self.cad_cliente)
        self.btn1.place(x=90, y=120)
        self.btn2 = Button(text='Buscar Cliente', font=font, width=23, height=2, bg='#204961', fg='white',
                           activebackground='#468AE8', command=self.busca_cliente)
        self.btn2.place(x=440, y=120)

        # BOTÕES OS
        self.btn3 = Button(text='Nova Ordem de Serviço', font=font, width=23, height=2, bg='#204961', fg='white',
                           activebackground='#468AE8', command=self.nova_os)
        self.btn3.place(x=90, y=220)
        self.btn4 = Button(text='Buscar Ordem de Serviço', font=font, width=23, height=2, bg='#204961', fg='white',
                           activebackground='#468AE8', command=self.busca_os)
        self.btn4.place(x=440, y=220)


        self.form.protocol("WM_DELETE_WINDOW", self.fechando)

    def cad_cliente(self):
        CadastroCliente()




    def busca_cliente(self):
        BuscarCliente()


    def nova_os(self):
        pass


    def busca_os(self):
        pass


    def fechando(self):
        if messagebox.askokcancel("Sair", "Deseja realmente sair do sistema?"):
            self.form.destroy()



root = Tk()
r = Inicio(root)
r.form.mainloop()
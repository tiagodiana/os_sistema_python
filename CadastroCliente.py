from tkinter import *
from tkinter import ttk
from Cliente import Cliente
from tkinter import messagebox


class CadastroCliente():
    message = messagebox

    def __init__(self):

        font = ('arial', 14, 'bold')
        estados = ['SP', 'AM']
        self.form = Tk()
        self.form.geometry('800x550+300+80')
        self.form.title('Cadastro de Cliente')
        self.form.resizable(0,0)
        self.form['bg'] = 'dodgerblue'

        #Label Titulo
        self.lblTitulo = Label(self.form, text='Cadastro de Cliente', font=('arial', 18, 'bold'), bg='#204961', fg='white')
        self.lblTitulo.pack(anchor=N, fill=X, ipady=15)

        #FORMULÁRIO
        #
        #NOME
        #
        self.lblnome = Label(self.form, text='Nome', font=font, bg='dodgerblue', fg='white')
        self.lblnome.place(x=100, y=100)
        self.txtnome = Entry(self.form, font=font, width=23)
        self.txtnome.focus_set()
        self.txtnome.place(x=100, y=130)
        #
        #CPF
        #
        self.lblcpf = Label(self.form, text='CPF', font=font, bg='dodgerblue', fg='white')
        self.lblcpf.place(x=460, y=100)
        self.txtcpf = Entry(self.form, font=font)
        self.txtcpf.place(x=460, y=130)
        #
        #TELEFONE
        #
        self.lbltelefone = Label(self.form, text='Telefone', font=font, bg='dodgerblue', fg='white')
        self.lbltelefone.place(x=100, y=180)
        self.txttelefone = Entry(self.form, font=font)
        self.txttelefone.place(x=100, y=210)
        #
        #CELULAR
        #
        self.lblcelular = Label(self.form, text='Celular', font=font, bg='dodgerblue', fg='white')
        self.lblcelular.place(x=460, y=180)
        self.txtcelular = Entry(self.form, font=font)
        self.txtcelular.place(x=460, y=210)
        #
        #RUA
        #
        self.lblrua = Label(self.form, text='Rua', font=font, bg='dodgerblue', fg='white')
        self.lblrua.place(x=100, y=260)
        self.txtrua = Entry(self.form, font=font, width=23)
        self.txtrua.place(x=100, y=290)
        #
        #NUM
        #
        self.lblnum = Label(self.form, text='N°', font=font, bg='dodgerblue', fg='white')
        self.lblnum.place(x=380, y=260)
        self.txtnum = Entry(self.form, font=font, width=5)
        self.txtnum.place(x=380, y=290)
        #
        #Bairro
        #
        self.lblbairro = Label(self.form, text='Bairro', font=font, bg='dodgerblue', fg='white')
        self.lblbairro.place(x=460, y=260)
        self.txtbairro = Entry(self.form, font=font)
        self.txtbairro.place(x=460, y=290)
        #
        #Cidade
        #
        self.lblcidade = Label(self.form, text='Cidade', font=font, bg='dodgerblue', fg='white')
        self.lblcidade.place(x=100, y=340)
        self.txtcidade = Entry(self.form, font=font)
        self.txtcidade.place(x=100, y=370)
        #
        #ESTADO
        #
        self.lblestado = Label(self.form, text="UF", font=font, bg='dodgerblue', fg='white')
        self.lblestado.place(x=360, y=340)
        self.cmbestado = ttk.Combobox(self.form, values=estados, width=5, height=2, font=font)
        self.cmbestado.current(0)
        self.cmbestado.place(x=360, y=370)
        #
        #CEP
        #
        self.lblcep = Label(self.form, text='CEP', font=font, bg='dodgerblue', fg='white')
        self.lblcep.place(x=460, y=340)
        self.txtcep = Entry(self.form, font=font)
        self.txtcep.place(x=460, y=370)
        #
        #BOTÃO SALVAR
        #
        self.btnsalvar = Button(self.form, text='Salvar', font=font, width=15, bg='#39804E', fg='#fff', activebackground='#94FFB4', command=self.btnSalvar)
        self.btnsalvar.place(x=290, y=450)


    def btnSalvar(self):
        #ESTANCIANDO A CLASSE CLIENTE
        self.c = Cliente()
        #PEGANDO OS VALORES DOS CAMPOS DE TEXTO DO FORMULARIO
        nome = self.txtnome.get()
        cpf = self.txtcpf.get()
        tel = self.txttelefone.get()
        cel = self.txtcelular.get()
        rua = self.txtrua.get() + '-' + self.txtnum.get()
        bairro = self.txtbairro.get()
        cidade = self.txtcidade.get()
        estado = self.cmbestado.get()
        cep = self.txtcep.get()
        self.c.inserirDados(nome, cpf, tel, cel, rua, bairro, cidade, estado, cep)
        self.confirmacao = messagebox.askokcancel('Confirmação', 'Deseja salvar esse cliente?')
        if self.confirmacao:
            try:
                self.result = self.c.cadUser()
                if self.result:
                    self.form.destroy()
                    print('Cliente Cadastrado com sucesso')
                    messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso!')
                else:
                    messagebox.showinfo('Erro', 'Erro ao cadastrar o cliente')
            except:
                messagebox.showinfo('ERRO', 'Erro no banco de dados')

if __name__ == '__main__':
    main = CadastroCliente()
    main.form.mainloop()

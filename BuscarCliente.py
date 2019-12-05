from tkinter import *
from tkinter import ttk
from Cliente import Cliente
from tkinter import messagebox


class BuscarCliente():
    def __init__(self):
        font = ('arial', 14, 'bold')
        estados = ['SP', 'AM']
        # Criando as variaveis para os campos de texto do formulario
        self.nome = StringVar()
        self.cpf = StringVar()
        self.tel = StringVar()
        self.cel = StringVar()
        self.rua = StringVar()
        self.num = StringVar()
        self.bairro = StringVar()
        self.cidade = StringVar()
        self.cep = StringVar()
        # ===========================================
        self.form =Toplevel()
        self.form.geometry('800x550+300+100')
        self.form.title('Buscar Cliente')
        self.form.resizable(0, 0)
        self.form['bg'] = 'dodgerblue'

        # Label Titulo
        self.lblTitulo = Label(self.form, text='Buscar Cliente', font=('arial', 18, 'bold'), bg='#204961', fg='white')
        self.lblTitulo.pack(anchor=N, fill=X, ipady=15)

        # FORMULÁRIO
        #
        # NOME
        #
        self.lblnome = Label(self.form, text='Nome', font=font, bg='dodgerblue', fg='white')
        self.lblnome.place(x=100, y=100)
        self.txtnome = Entry(self.form, font=font, width=23, state='disabled', textvariable=self.nome)
        self.txtnome.place(x=100, y=130)
        #
        # CPF
        #
        self.lblcpf = Label(self.form, text='CPF', font=font, bg='dodgerblue', fg='white')
        self.lblcpf.place(x=460, y=100)
        self.txtcpf = Entry(self.form, font=font, textvariable=self.cpf)
        self.txtcpf.focus_set()
        self.txtcpf.place(x=460, y=130)
        #
        # TELEFONE
        #
        self.lbltelefone = Label(self.form, text='Telefone', font=font, bg='dodgerblue', fg='white')
        self.lbltelefone.place(x=100, y=180)
        self.txttelefone = Entry(self.form, font=font, state='disabled', textvariable=self.tel)
        self.txttelefone.place(x=100, y=210)
        #
        # CELULAR
        #
        self.lblcelular = Label(self.form, text='Celular', font=font, bg='dodgerblue', fg='white')
        self.lblcelular.place(x=460, y=180)
        self.txtcelular = Entry(self.form, font=font, state='disabled', textvariable=self.cel)
        self.txtcelular.place(x=460, y=210)
        #
        # RUA
        #
        self.lblrua = Label(self.form, text='Rua', font=font, bg='dodgerblue', fg='white')
        self.lblrua.place(x=100, y=260)
        self.txtrua = Entry(self.form, font=font, width=23, state='disabled', textvariable=self.rua)
        self.txtrua.place(x=100, y=290)
        #
        # NUM
        #
        self.lblnum = Label(self.form, text='N°', font=font, bg='dodgerblue', fg='white')
        self.lblnum.place(x=380, y=260)
        self.txtnum = Entry(self.form, font=font, width=5, state='disabled', textvariable=self.num)
        self.txtnum.place(x=380, y=290)
        #
        # Bairro
        #
        self.lblbairro = Label(self.form, text='Bairro', font=font, bg='dodgerblue', fg='white')
        self.lblbairro.place(x=460, y=260)
        self.txtbairro = Entry(self.form, font=font, state='disabled', textvariable=self.bairro)
        self.txtbairro.place(x=460, y=290)
        #
        # Cidade
        #
        self.lblcidade = Label(self.form, text='Cidade', font=font, bg='dodgerblue', fg='white')
        self.lblcidade.place(x=100, y=340)
        self.txtcidade = Entry(self.form, font=font, state='disabled', textvariable=self.cidade)
        self.txtcidade.place(x=100, y=370)
        #
        # ESTADO
        #
        self.lblestado = Label(self.form, text="UF", font=font, bg='dodgerblue', fg='white')
        self.lblestado.place(x=360, y=340)
        self.cmbestado = ttk.Combobox(self.form, values=estados, width=5, height=2, font=font, state='disabled')
        self.cmbestado.current(0)
        self.cmbestado.place(x=360, y=370)
        #
        # CEP
        #
        self.lblcep = Label(self.form, text='CEP', font=font, bg='dodgerblue', fg='white')
        self.lblcep.place(x=460, y=340)
        self.txtcep = Entry(self.form, font=font, state='disabled', textvariable=self.cep)
        self.txtcep.place(x=460, y=370)
        #
        # BOTÃO BUSCAR
        #
        self.btnbuscar = Button(self.form, text='Buscar', font=font, width=10, bg='#2772CC', fg='#fff',
                                activebackground='#308DFF', command=self.buscarUSER)
        self.btnbuscar.place(x=250, y=450)
        #
        # BOTÃO ALTERAR
        #
        self.btnalterar = Button(self.form, text='Alterar', font=font, width=10, bg='#CCB81D', fg='#fff',
                                 activebackground='#FFE623', state='disabled', command=self.btnAlterar)
        self.btnalterar.place(x=390, y=450)

    # FUNCÃO BOTÃO BUSCAR
    def buscarUSER(self):
        c = Cliente()
        self.dados = c.buscaUser(self.txtcpf.get())
        end = self.dados[5].split('-')
        self.ativarTexto()
        self.btnalterar['state'] = 'normal'
        # Setando as variaveis
        self.nome.set(self.dados[1])
        self.cpf.set(self.dados[2])
        self.tel.set(self.dados[3])
        self.cel.set(self.dados[4])
        self.rua.set(end[0])
        self.num.set(end[1])
        self.bairro.set(self.dados[6])
        self.cidade.set(self.dados[7])
        self.cmbestado.set(self.dados[8])
        self.cep.set(self.dados[9])
        self.btnbuscar['state'] = 'disabled'


    def btnAlterar(self):
        nome = self.txtnome.get()
        cpf = self.txtcpf.get()
        tel = self.txttelefone.get()
        cel = self.txtcelular.get()
        rua = self.txtrua.get() + '-' + self.txtnum.get()
        bairro = self.txtbairro.get()
        cidade = self.txtcidade.get()
        estado = self.cmbestado.get()
        cep = self.txtcep.get()
        c = Cliente()
        c.inserirdadosid(self.dados[0], nome, cpf, tel, cel, rua, bairro, cidade, estado, cep)
        confirm = messagebox.askokcancel("Confirmação", 'Deseja alterar os dados desse Cliente?')
        if confirm:
            result = c.alterarCliente()
            if result:
                messagebox.showinfo('Sucesso', 'Alterações feitas com sucesso')
                self.btnalterar['state'] = 'disabled'
                self.btnbuscar['state'] = 'normal'
                self.limpaCampos()
            else:
                messagebox.showerror('Erro', 'Não foi possivel alterar os dados, contate um administrador!')


    def ativarTexto(self):
        self.txtnome['state'] = 'normal'
        self.txttelefone['state'] = 'normal'
        self.txtcelular['state'] = 'normal'
        self.txtrua['state'] = 'normal'
        self.txtnum['state'] = 'normal'
        self.txtbairro['state'] = 'normal'
        self.txtcidade['state'] = 'normal'
        self.cmbestado['state'] = 'normal'
        self.txtcep['state'] = 'normal'



    def limpaCampos(self):
        # Setando as variaveis
        self.nome.set('')
        self.cpf.set('')
        self.tel.set('')
        self.cel.set('')
        self.rua.set('')
        self.num.set('')
        self.bairro.set('')
        self.cidade.set('')
        self.cmbestado.set('')
        self.cep.set('')
        self.txtnome['state'] = 'disabled'
        self.txttelefone['state'] = 'disabled'
        self.txtcelular['state'] = 'disabled'
        self.txtrua['state'] = 'disabled'
        self.txtnum['state'] = 'disabled'
        self.txtbairro['state'] = 'disabled'
        self.txtcidade['state'] = 'disabled'
        self.cmbestado['state'] = 'disabled'
        self.txtcep['state'] = 'disabled'


if __name__ == '__main__':
    buscacliente = BuscarCliente()
    buscacliente.form.mainloop()

from Conexao import Conexao
from tkinter import messagebox


# CLASSE CLIENTE HERDA A CLASSE CONEXAO
class Cliente(Conexao):
    id = ''
    nome = ''
    cpf = ''
    tel = ''
    cel = ''
    rua = ''
    bairro = ''
    cidade = ''
    estado = ''
    cep = ''

    def __int__(self):
        Conexao.__init__(self)

    # INSERINDO DADOS DO CLIENTE
    def inserirDados(self, name, cpf, tel, cel, rua, bairro, cidade, estado, cep):
        self.nome = name
        self.cpf = cpf
        self.tel = tel
        self.cel = cel
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def inserirdadosid(self,id, name, cpf, tel, cel, rua, bairro, cidade, estado, cep):
        self.id = id
        self.nome = name
        self.cpf = cpf
        self.tel = tel
        self.cel = cel
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    # FUNÇÃO PARA CADASTRAR CLIENTE
    def cadUser(self):
        try:
            sql = 'INSERT INTO clientes VALUES(null,%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (
                self.nome, self.cpf, self.tel, self.cel, self.rua, self.bairro, self.cidade, self.estado, self.cep))
            self.conn.commit()
            self.conn.close()
            return True

        except:
            return False

    def buscaUser(self, cpf):
        self.cpf = cpf
        if cpf != "":
            sql = 'SELECT * FROM clientes WHERE cpf LIKE %s'
            self.cursor.execute(sql % self.cpf)
            result = self.cursor.fetchone()
            self.conn.close()
            return result
        else:
            messagebox.showinfo("Erro", "Digite o cpf do Cliente")

    def alterarCliente(self):
        try:
            sql = 'UPDATE clientes SET nome = %s, cpf = %s, telefone = %s, celular = %s, rua = %s, bairro = %s, cidade = %s, estado = %s, cep = %s WHERE id = %s'
            self.cursor.execute(sql, (self.nome, self.cpf, self.tel, self.cel, self.rua, self.bairro, self.cidade, self.estado, self.cep, int(self.id)))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            print('Erro ao atualizar')
            return False
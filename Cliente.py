from Conexao import Conexao

#CLASSE CLIENTE HERDA A CLASSE CONEXAO
class Cliente(Conexao):
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


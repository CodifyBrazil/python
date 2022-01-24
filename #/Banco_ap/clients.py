import database3
import random


clients = {'123.456.789-00':
        {'Id_banco': 'Itau', 'Agencia': '0123', 'Conta': '0458', 'Cliente': 'Julio Almeida', 'Saldo': 0},
    '987.654.321-00':
    {'Id_banco': 'Caixa Economica', 'Agencia': '0154', 'Conta': '0148', 'Cliente': 'Fausto Alencar', 'Saldo': 0},
    '123.456.789-01':
    {'Id_banco': 'Santander', 'Agencia': '0164', 'Conta': '0146', 'Cliente': 'Bruno Souza', 'Saldo': 0},
    '123.45.789-02':
    {'Id_banco': 'NuBank', 'Agencia': '0648', 'Conta': '0163', 'Cliente': 'Camila Alves', 'Saldo': 0},
            '123.456.789-03':
    {'Id_banco': 'Banco do Brasil', 'Agencia': '0184', 'Conta': '0954', 'Cliente': 'Gisele Suzano', 'Saldo': 0},
}

tranfer = {
    'HashTransferenciaUnica':{
        'CPF_Origem': {'Id_banco': 'Itau', 'data/hora': 'data/hora'},
        'CPF_destino': {'Id_banco': 'Itau', 'data/hora': 'data/hora'},
        'Valor': 10
        }
}

deposit = {'data/hora': {'agencia': 'agencia', 'conta':'conta', 'Valor': 'valor'}
}


class Bank:

#Nome do nosso banco = Direct Bank
#Agencia padrao Direct Bank = 00001

    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.id_banco = 'Direct Bank'
        self.agencia = '00001'
        self.conta_corrente = 0
        self.saldo = 0

    def create_account(self, nome, cpf):
        '''
        :param self: Class
        :param nome: nome do cliente
        :param cpf: cpf do cliente
        :return: retorna dados do cliente criado (nome, banco, cpf, saldo, agencia, conta)
        '''

        if nome != '' or nome != ' ' and cpf.isnumeric():
            self.nome = nome
            self.cpf = cpf
            self.conta_corrente = random.randrange(10000, 99999)
            clientes[cpf] = {'Id_banco': self.id_banco, 'Agencia': self.agencia, 'Conta': self.conta_corrente, 'Cliente': self.nome, 'Saldo': self.saldo}

            mensage = 'Cliente cadastrado com sucesso!'
            return mensage
        else:
            return 'Erro, o usuario NÂO foi criado!'

    def clients_view(self, cpf=''):

        if cpf != '' or cpf != ' ':
            DB = database3.Database()
            clients = DB.get_clients_all()

            client_info = []

            for ck, cv in clients.items():
                print(ck, cv)



        else:
            return 'Digite um CPF.'


    def deposit(self):
        pass





b = Bank()

print(b.clients_view('123.456.789-01'))



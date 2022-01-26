import database3
import random

class Bank:

#Nome do nosso banco = Direct Bank
#Agencia padrao Direct Bank = 00001

    def __init__(self):
        self.name = ''
        self.cpf = ''
        self.id_bank = 'Direct Bank'
        self.agency = '00001'
        self.account = 0
        self.balance = 0
        self.database = database3.Database()
        self.loggin = False

    def start_bank(self):
        if self.loggin == False:
            print('''
                ###########################################################
                ##################### DIRECT BANK #########################
                ###########################################################
                
                Seja bem vindo, escolha as opções abaixo:
                
                [ 1 ] - Entrar em minha conta
                [ 2 ] - Criar minha conta
            
            ''')

        options = input('Digite sua opção: ')

        if options == 1:
            




    def create_account(self, name, cpf):
        '''
        :param self: Class
        :param nome: nome do cliente
        :param cpf: cpf do cliente
        :return: retorna dados do cliente criado (nome, banco, cpf, saldo, agencia, conta)
        '''

        if name != '' or name != ' ' and cpf.isnumeric():
            self.name = name
            self.cpf = cpf
            self.account = random.randrange(10000, 99999)

            if self.database.create_account(name=name, cpf=cpf, id_bank=self.id_bank, agency=self.agency, account=self.account, balance=0, type_data='client_account'):
                mensage = 'Cliente cadastrado com sucesso!'
                return mensage
            else:
                return 'ERRO! O usuario NÂO foi criado!'
        else:
            print('Erro! nome vazio ou cpf invalido.')

    def clients_view(self, cpf=''):
        '''
        :param cpf: insera um CPF para ser consultado.
        :return: retorna os dados do cliente.
        '''

        if cpf != '' and cpf != ' ':
            response = self.database.check_costumer_exists(cpf)

            if response:
                return True
            else:
                return False
        else:
            return 'Digite um cpf'


    def deposit(self):
        pass




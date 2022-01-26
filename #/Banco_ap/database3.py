'''
MODULO DE CONEXAO COM FIREBASE
'''


import requests
import security
from datetime import datetime
import json


class Database:

    def __init__(self):
        self.security = security.Security()
        self.acess_link = 'https://banking-london-default-rtdb.firebaseio.com/.json'
        self.hash_token = self.security.hash_generator_uuid()
        self.date_time = datetime.today().strftime('%H-%m-%d %H:%M:%S')

    def check_costumer_exists(self, cpf=''):
        '''
            Checa se o usuario existe através do CPF


        :param cpf: CPF do usuarioi que deseja ver se existe
        :return: retorna True para existente, e False para Inexistente
        '''

        if cpf != '' and cpf != ' ':
            request = requests.get(self.acess_link)
            request = request.json()
            cks = [ck for ck, cv in request.items()]

            for i in cks:
                for k, v in request[i].items():
                    if k == cpf:
                        if v['type_data'] == 'Client_account':
                            print(k, v)
                        print('----------------------')


    def get_clients_all(self):
        request = requests.get(self.acess_link)
        request = request.json()
        return request[1]

    def create_account(self, name='', cpf='', id_bank='Direck Bank', agency=10001, account=0, balance=0, type_data='client_account'):
        if cpf != '' and cpf != ' ' and len(name) > 1:
            '''
                {
                  'Id_banco': self.id_banco,
                  'Agencia': self.agencia,
                  'Conta': self.conta_corrente,
                  'Cliente': self.nome,
                  'Saldo': self.saldo
                }
            '''
            data = {cpf:{'Id_bank': id_bank, 'Agency': agency, 'Account': account, 'Client_name': name, 'Balance': balance, 'Date_time_create_account': self.date_time, 'type_data': 'Client_account'}}
            data = json.dumps(data)
            request = requests.post(self.acess_link, data)
            return request


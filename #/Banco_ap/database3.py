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
        self.acess_link = ''
        self.hash_token = self.security.hash_generator_uuid()
        self.date_time = datetime.today().strftime('%H-%m-%d %H:%M:%S')

    def check_costumer_exists(self, cpf=''):
        if cpf != '' and cpf != ' ':
            request = requests.get(self.acess_link)
            request = request.json()
            list_cpfs = []

            for i in range(1, len(request)):
                for ck, cv in request[i].items():
                    if ck == 'cpf':
                        list_cpfs.append(cv)


        if cpf in list_cpfs:
            return True

        else:
            return False

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
            data = {'Id_bank': id_bank, 'Agency': agency, 'Account': account, 'Client_name': name, 'Balance': balance, 'Date_time_create_account': self.date_time, 'type_data': type_data}
            data = json.dumps(data)
            request = requests.post(self.acess_link, data)
            return request


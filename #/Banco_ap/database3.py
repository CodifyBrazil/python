'''
MODULO DE CONEXAO COM FIREBASE
'''


import requests
import hashlib
import random


class Database:

    def __init__(self):
        self.acess_link = 'https://banking-london-default-rtdb.firebaseio.com/.json'
        string = str(random.randrange(1000000000000, 999999999999999999)).encode()
        self.hash_token = hashlib.md5(string).hexdigest()

    def check_costumer_exists(self, cpf=''):
        if cpf != '' and cpf != ' ':
            request = requests.get(self.acess_link)
            request = request.json()
            request = request[1]

            for ck, cv in request.items():
                print(ck['Name_client'])



    def get_clients_all(self):
        request = requests.get(self.acess_link)
        request = request.json()
        return request[1]

    def create_account(self):
        pass


d = Database()
print(d.check_costumer_exists('123.456.789.01'))
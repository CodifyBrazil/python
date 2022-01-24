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

    def get_clients_all(self):
        request = requests.get(self.acess_link)
        return request.json()
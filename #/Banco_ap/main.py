import clients as cl
import security

Bank = cl.Bank()

name = input('Por favor digite seu nome: ')
cpf = input('Por favor digite seu CPF (apenas numeros): ')

response = Bank.create_account(name, cpf)











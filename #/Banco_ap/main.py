import clients as cl

Bank = cl.Bank()

client = Bank.clients_view(cpf='123.456.789-01')
print(client)










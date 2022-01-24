preco_produtos = [350, 400, 250, 670]
produtos = ['Cafe', 'Pao', 'Liquidificador', 'Serra']
n = []
lista = [(i * 0.3)+i for i in preco_produtos]

print(lista)

for v in preco_produtos:
    valor = v * 0.3
    v = valor + v
    n.append(v)

print(n)
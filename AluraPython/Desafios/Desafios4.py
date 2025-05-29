preco1 = float(input('digite o preco do caro no 1 ano:'))
preco2 = float(input('digite o preco do caro no 2 ano:'))
preco3 = float(input('digite o preco do caro no 3 ano:'))

maior = max(preco1, preco2 ,preco3)
menor = min(preco1, preco2 ,preco3)
print(f'O maior preco do carro foi {maior}')
print(f'O menor preco do carro foi {menor}')
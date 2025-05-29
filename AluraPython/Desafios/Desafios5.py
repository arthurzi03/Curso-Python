

nome = str('produto1, produto2, produto3')

produto1 = float(input('Digite o preço do produto 1: '))
produto2 = float(input('Digite o preço do produto 2: '))    
produto3 = float(input('Digite o preço do produto 3: '))

menor = min(produto1, produto2, produto3)
print(f'O menor preço é:,{menor}')
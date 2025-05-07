nota1 = input('digite a primeira nota:')
nota2 = input('digite a segunda nota:')
nota3 = input('digite a terceira nota:')

# Convertendo as notas para float
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

# Calculando a média
media = (nota1 + nota2 + nota3) / 3

# Imprimindo a média
print('A média das notas é:', media)
# Calculando a média ponderada
numeros = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]

soma_ponderada = sum(numero * peso for numero, peso in zip(numeros, pesos))
soma_pesos = sum(pesos)

media_ponderada = soma_ponderada / soma_pesos

# Imprimindo a média ponderada
print('A média ponderada dos números é:', media_ponderada)
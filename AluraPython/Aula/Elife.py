# Verifica se um número é positivo, negativo ou zero
numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Verifica se um número é par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
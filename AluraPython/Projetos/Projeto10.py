
Operacao = input("Digite a operação desejada (+, -, *, /): ")

Numero1 = int(input("Digite o primeiro número: "))
Numero2 = int(input("Digite o segundo número: "))


if Operacao == '+':
    resulado = Numero1 + Numero2
elif Operacao == '-':
    resulado = Numero1 - Numero2
elif Operacao == '*':
    resulado = Numero1 * Numero2
elif Operacao == '/':
    if Numero2 == 0:
        resulado = "Erro: Divisão por zero não é permitida."
    else:
        resulado = Numero1 / Numero2
print('o resulatdo é:',resulado)
if resulado %2 == 0:
    print("O resultado é par.")
else:
    print("O resultado é ímpar.")
if resulado > 0:
    print("O resultado é positivo.")
elif resulado < 0:
    print("O resultado é negativo.")
if resulado == int(resulado):
    print("O resultado é um número inteiro.")
else:
    print("O resultado é um número decimal.")
numero = int (input("Digite um número: "))
numero2 = int (input("Digite outro número: "))
numero3 = int (input("Digite mais um número: "))

equilatero = (numero == numero2) and (numero == numero3) and (numero2 == numero3)
isósceles = (numero == numero2) or (numero == numero3) or (numero2 == numero3)
escaleno = (numero == numero2) or (numero == numero3) or (numero2 == numero3)

if equilatero:
    print("O triângulo é equilatero.")
elif isósceles:
    print("O triângulo é isósceles.")
elif escaleno:
    print("O triângulo é escaleno.")
else:
    print('O triângulo é escaleno.')

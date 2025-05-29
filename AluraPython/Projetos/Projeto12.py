# Entrada de dados
litros = float(input("Quantidade de litros: "))
tipo = input("Tipo de combustível (E para etanol, D para diesel): ").upper()

# Preços por litro
preco_etanol = 1.70
preco_diesel = 2.00

# Cálculo do valor a ser pago
if tipo == "E":
    preco_litro = preco_etanol
    if litros <= 15:
        desconto = 0.02
    else:
        desconto = 0.04
elif tipo == "D":
    preco_litro = preco_diesel
    if litros <= 15:
        desconto = 0.03
    else:
        desconto = 0.05
else:
    print("Tipo de combustível inválido.")
    exit()

# Calculando valores
valor_bruto = preco_litro * litros
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

# Resultado
print(f"\nValor bruto: R$ {valor_bruto:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")

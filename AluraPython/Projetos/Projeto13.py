vendas2022 = int(input("Digite o valor das vendas de 2022: "))
vendas2023 = int(input("Digite o valor das vendas de 2023: "))

variacao =((vendas2023 - vendas2022) / vendas2022) * 100
if variacao > 0:
    print(f"A empresa teve um crescimento de {variacao:.2f}% nas vendas de 2022 para 2023.")    
if variacao >20:
    print("A empresa teve um crescimento excelente nas vendas.")
elif 2 < variacao <= 20:
    print("A empresa teve um crescimento moderado nas vendas.")
elif - 20 < variacao <= 2:
    print("A empresa teve um crescimento baixo nas vendas.")
else:
    print("A empresa teve uma queda nas vendas.")
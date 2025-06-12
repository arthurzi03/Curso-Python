bacteriaA = 4
bacteriaB = 8
dias = 0
while bacteriaA < bacteriaB:
    bacteriaA *= 1.03
    bacteriaB *= 1.015
    dias += 1
    print(f'Dia {dias}: Bactéria A tem {bacteriaA:.2f} unidades, Bactéria B tem {bacteriaB:.2f} unidades.')
print(f'Foram necessários {dias} dias para que a Bactéria A superasse a Bactéria B.')
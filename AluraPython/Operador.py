t1 = t2 =True
f1 = f2 = False
if t1 and t2: #vai dar verdadeiro se ambos forem verdadeiros
    print("são verdadeiros")
else:
    print("não são verdadeiros")



t1 = t2 =True
f1 = f2 = False
if f1 or f2: #vai dar falsa se ambos forem falsos
    print("são verdadeiros")
else:
    print("não são verdadeiros")




t1 = t2 =True
f1 = f2 = False
if  not f2: #ele vai true para false e false para true
    print("são verdadeiros")
else:
    print("não são verdadeiros")



lista = 'Maria', 'João', 'José', 'Ana', 'Pedro'
nome_1 = 'Maria'
nome_2 = 'João'
if nome_1 in lista: #verifica se o nome está na lista
    print("O nome", nome_1, "está na lista")
else:
    print("O nome", nome_1, "não está na lista")
if nome_2 in lista: #verifica se o nome está na lista
    print(f' {nome_2}, está na lista')
else:
    print(f' {nome_2}, não está na lista')



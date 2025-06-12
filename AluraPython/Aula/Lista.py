Lista = ['Fabricio Daniel', 9.5,9.0,90,True]
print(Lista[0])



Lista[3]=10.0
print(Lista)

media = (Lista[1] + Lista[2] + Lista[3]) / 3
print(media)


len (Lista)
Lista [:3] # Pega os 3 primeiros elementos


Lista.append(media) # Adiciona o elemento media no final da lista
print(Lista)

Lista.extend(['Python', 'Java']) # Adiciona os elementos Python e Java no final da lista
print(Lista)

Lista.append(['Python', 'Java']) # Adiciona a lista ['Python', 'Java'] no final da lista
print(Lista)


Lista.remove('Fabricio Daniel') # Remove o elemento 'Fabricio Daniel' da lista  
print(Lista)
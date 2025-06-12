dicionario = {'chave1':1,
               'chave2':2}
print(dicionario['chave1'])  # Acessa o valor associado à chave 'chave1'


cadastro = {'matricula':123,
            'dia':10,
            'mes':10,
            'turma':'2A'}
print(cadastro)
print(cadastro['matricula'])  # Acessa o valor associado à chave 'matricula'
print(cadastro['dia'])       # Acessa o valor associado à chave 'dia'       
print(cadastro['mes'])       # Acessa o valor associado à chave 'mes'
print(cadastro['turma'])     # Acessa o valor associado à chave 'turma'

cadastro['turmma']='2B'
print(cadastro)  # Imprime o dicionário atualizado com a nova chave 'turmma'

cadastro['modalidade']='ead'
print(cadastro)  # Imprime o dicionário atualizado com a nova chave 'modalidade'
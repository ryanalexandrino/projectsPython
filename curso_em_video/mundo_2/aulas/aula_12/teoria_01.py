# Condições Aninhadas

# Lê un nome do usuário
nome = str(input('Qual o seu nome? '))

# Cria um estrutrura condicional aninhada para personalizar uma resposta, com base no nome inserido
if nome == 'Ryan':
    print('Que coincidência, seu nome é o mesmo que o meu! Muito prazer chara!')
elif nome == 'Verônica':
    print('Você tem o mesmo nome da minha prima! Muito prazer')
else:
    print(f'Muito prazer em te conhecer, {nome}!')
print('Tenha um excelente dia!!')


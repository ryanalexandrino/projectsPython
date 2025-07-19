# Estrutura de Repetição
# Laço for usando variaveis

# Lê um número do usuário
numero = int(input('Digite um número: '))

# Execução padrão
for c in range(0, numero):
    print(f'{c} - Olá!!')
print('Fim! \n')

# Lê todos os passoas da iteração
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

# Execução com base nas variavéis
for c in range(i, f+1, p):
    print(f'{c} - Olá!!')
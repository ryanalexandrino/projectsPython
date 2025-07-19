# A Confederação Nacional de Natação precisa de um programa que leia leia ano de nascimento dele
# Mostre sua categoria de acordo com a idade
# Até 9 anos - MIRIM
# Até 14 anos - INFANTIL
# Até 19 anos - JUNIOR
# Até 25 anos - SÊNIOR
# Acima - MASTER

# Importa o módulo de datas
from datetime import date

# Lê ano de nascimento do nadador
ano_nascimento = int(input('Digite o seu ano de nascimento: '))

# Calcula a idade com base no ano de nascimento
idade = date.today().year - ano_nascimento

# Cria uma condicional aninhada que define a categoria com base na idade
if idade <= 9:
    print(f'O nadador possui {idade} anos, e faz parte da categoria MIRIM!')
elif idade > 9 and idade <= 14:
    print(f'O nadador possui {idade} anos, e faz parte da categoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'O nadador possui {idade} anos, e faz parte da categoria JUNIOR!')
elif idade > 19 and idade <= 25:
    print(f'O nadador possui {idade} anos, e faz parte da categoria SÊNIOR!')
else:
    print(f'O nadador possui {idade} anos, e faz parte da categoria MASTER!')

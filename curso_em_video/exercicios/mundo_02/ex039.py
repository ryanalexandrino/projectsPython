# Faça um programa que leia a data de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se já é hora de se alistar ao serviço militar
# Se já passou o tempo de se alistar
# O programa também deverá mostrar (em anos) quanto tempo falta ou já passou para o alistamento

# importa o módulo de data, função de ano
from datetime import date

# Lê a data de nascimento do jovem usuario e a converte em anos de idade
data_nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - data_nascimento

# Cria a condicional aninhada que verifica a situação de alistamento
if idade < 18:
    saldo_anos = 18 - idade
    print(f'Ainda não é hora de se alistar.. \n'
          f'Ainda faltam {saldo_anos} anos para seu alistamento! \n'
          f'Seu ano de alistamento será em {date.today().year + saldo_anos}')
elif idade == 18:
    print(f'Já é hora de se alistar, você já possui {idade} anos!')
else:
    saldo_anos = idade - 18
    print(f'Já passou seu prazo de alistamento! \n'
          f'Você se atrasou {saldo_anos} anos para seus alistamento! \n'
          f'Seu ano de alistamento foi em {date.today().year - saldo_anos}')

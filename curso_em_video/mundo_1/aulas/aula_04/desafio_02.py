# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia = input('Qual o dia que você nasceu? ')
mes = input('Em qual mês? ')
ano = int(input('De qual ano? '))
# Opcional
idade = 2023 - ano

print('Entendi!, você nasceu em', dia, 'de', mes, 'de', ano)
# Opcional
print('Provavelmente você tem', idade, 'anos. Certo?')

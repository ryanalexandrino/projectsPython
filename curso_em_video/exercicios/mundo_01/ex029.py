# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h mostre uma mensagem que ele foi multado
# A multa vai custar R$ 7,00 por cada Km acima do permitido

# Lê a velocidade do carro
velocidade = float(input('Qual velocidade o carro estava? '))

# Cria uma condicional que verifica se o carro será multado
if velocidade > 80:
    multa = float(velocidade - 80) * 7
    print(f'\nVocê está acima da velocidade! \n'
          f'Você foi multado em: R$ {multa:.2f}')
else:
    print('\nVocê está dentro do limite de velocidade!')
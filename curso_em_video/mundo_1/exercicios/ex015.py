# Escreva um programa que pergunte a quantidade de KM percorridos e dias alugados de um carro
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e 0,15 por KM rodado

# Pede o numero de dias alugados e KM´s rodados
dias = int(input('Digite a quantidade de dias em que o carro foi alugado: '))
kms = float(input('Digite a kilometragem percorrida nesse período: '))

# Calcula o valor a pagar com base nas informações inseridas
valor = (dias * 60) + (kms * 0.15)

# Exibe o valor a ser pago ao usuário
print(f'Com base nas informações inseridas, o valor total a pagar foi de: R$ {valor:.2f}')


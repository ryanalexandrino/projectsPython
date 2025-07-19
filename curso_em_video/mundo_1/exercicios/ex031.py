# Desenvolva um programa que pergunte a distância de uma viagem em Km
# Calcule o preço da passagem, cobrando por KM:
# O valor de R$ 0,50 para viagens de até 200Km e R$ 0,40 para viagens mais longas

# Lê a distância da viagens em KM
distancia = int(input('Digite qual a distância da sua viagem: '))

# Analisa e calcula o valor com base na distancia
if distancia <= 200:
    valor = float(distancia * 0.50)
    print(f'Com base na distância da viagem ({distancia}KM) o valor a pagar é de R${valor:.2f}')
else:
    valor = float(distancia * 0.45)
    print(f'Com base na distância da viagem ({distancia}Km) o valor a pagar é de R${valor:.2f}')
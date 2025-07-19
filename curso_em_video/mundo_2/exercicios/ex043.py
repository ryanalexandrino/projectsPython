# Desenvolva uma lógica que leia o peso e altura de uma pessoa.
# Calcule seu IMC e mostre o status de acordo com as opções abaixo:
# Abaixo de 18.5 - Abaixo do peso
# Entre 18.5 e 25 - Peso ideal
# 25 até 30 - Sobrepeso
# 30 até 40 - Obesidade
# Acima de 40 - Obesidade mórbida

# Lê o peso e altura do usuário
peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (M): '))

# Calcula o IMC do usuário
imc = peso / (altura**2)

# Cria uma condicional aninhada que exibe a classificação do IMC do usuário
if imc < 18.5:
    print(f'Seu Índice de Massa Corporal: {imc:.2f} \n'
          f'Você está Abaixo do Peso!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu Índice de Massa Corporal: {imc:.2f} \n'
          f'Você está em seu Peso Ideal!')
elif imc >= 25 and imc < 30:
    print(f'Seu Índice de Massa Corporal: {imc:.2f} \n'
          f'Você está com Sobrepeso!')
elif imc >= 30 and imc < 40:
    print(f'Seu Índice de Massa Corporal: {imc:.2f} \n'
          f'Você está Obeso!')
elif imc >= 40:
    print(f'Seu Índice de Massa Corporal: {imc:.2f} \n'
          f'Você está com Obesidade mórbida!')

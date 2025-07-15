# Escreva um programa que leia o sálario de um funcionário e calcule seu aumento
# Para sálarios superiores a R$1.250,00 calcule um aumento de 10%
# Para sálatios inferiores ou iguais a R$1.250,00 calcule um aumento de 15%

# Lê o sálario do usuário
salario = float(input('Digite o seu sálario: '))

# Cria uma condicional para calcular o aumento e exibi-lo
if salario > 1250:
    aumento = salario * 0.10
    novo_salario = aumento + salario
    print(f'Você recebeu um aumento de R${aumento:.2f} (10%), totalizando R${novo_salario:.2f}!')
else:
    aumento = salario * 0.15
    novo_salario = aumento + salario
    print(f'Você recebeu um aumento de R${aumento:.2f} (15%), totalizando R${novo_salario:.2f}!')
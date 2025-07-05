#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário com um aumento de 15%
#Pede o valor do sálario ao usuário
salario = float(input('Digite o valor do sálario: '))
#Calcula o aumento e o exibe ao usuário
print(f'O sálario com um aumento de 15% totaliza R$ {salario + (0.15 * salario):.2f}')
#Faça um programa que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto
#Pede o preço do produto ao usuário
preco = float(input('Digite o preço do produto: R$ '))
#Calcula e mostra o preço com desconto
print(f'O preço do produto com desconto de 5% é de R$ {preco - (preco * 5 / 100):.2f}')
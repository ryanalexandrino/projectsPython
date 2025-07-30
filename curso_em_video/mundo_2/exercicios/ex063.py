# Escreva um programa que leia um número "n" na tela
# Mostre na tela os "n" primeiros elementos de uma sequência fibonacci

# Variavéis de controle do laço
limite = int(input('Digite o número de termos da sequência: '))
termo_atual = 0
proximo_termo = 1

# Cra um laço com a lógica do fibonacci
while termo_atual <= limite :
    soma = termo_atual + proximo_termo
    termo_atual = proximo_termo
    proximo_termo = soma
    print(soma)

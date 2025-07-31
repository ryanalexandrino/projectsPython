# Escreva um programa que leia um número "n" na tela
# Mostre na tela os "n" primeiros elementos de uma sequência fibonacci

# Variáveis de controle do laço
limite = int(input('Digite o número de termos da sequência: '))
t1 = 0
t2 = 1
contador = 3

# Exibe os termos neutros da sequencia
print(f" {t1} -> {t2}", end='')

# Cra um laço com a lógica do fibonacci
while  contador <= limite :
    f = t1 + t2
    print(f" -> {f}", end='')
    t1 = t2
    t2 = f
    contador += 1
print(' -> Fim!')

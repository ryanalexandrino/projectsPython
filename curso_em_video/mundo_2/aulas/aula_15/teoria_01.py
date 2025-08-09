# Exemplo simples de uso de interrupção de laço while

# Inicializa a variável soma

# Laço infinito que só é interrompido ao digitar o número 999
while True:
    numero = int(input('Digite um número:'))
    if numero == 999:
        break
    else:
        soma +=m
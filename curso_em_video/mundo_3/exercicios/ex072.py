# Crie uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso

numeros_extensos = ('zero',
                    'um', 'dois', 'tres', 'quatro', 'cinco',
                    'seis', 'sete', 'oito', 'nove', 'dez',
                    'onze', 'doze', 'treze', 'quatrorze', 'quinze',
                    'dezesseis', 'dezessete,' 'dezoito', 'dezenove',
                    'vinte')

numero = -1

while numero < 0 or numero > 20:
    numero = int(input('Digite um número de 0 a 20: '))
    if numero < 0 or numero > 20:
        print('Opção inválida! Digite novamente..')

print(f'O número digitado por extenso é {numeros_extensos[numero]}!')

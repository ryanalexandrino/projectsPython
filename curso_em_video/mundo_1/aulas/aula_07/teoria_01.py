
# Operadores Aritméticos

# Pede os números ao usuário
print('Insira dois numero a seguir, o primeiro deve ser maior que o segundo!')
numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

# Realiza as operações com os número digitados
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
exponenciacao = numero1 ** numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2

#Mostra os valores calculados nas variaveis acima
print(f'A soma dos numeros é: {soma} \n'
      f'O produto é: {multiplicacao} \n'
      f'A exponenciação é: {exponenciacao} \n'
      f'A divisão é: {divisao:.2f} \n'
      f'A divisão inteira é: {divisao_inteira}')


#Pede o primeiro numero ao usuario
numero1 = int(input('Digite o primeiro número: '))
#Mostra o tipo de dado da primeira variavel
print(type(numero1))

#Pede o segundo numero ao usuario
numero2 = int(input('Digite o segundo número: '))
#Mostra o tipo de dado da segunda variavel
print(type(numero2))

#Soma os dois numeros
soma = numero1 + numero2

#Mostra a soma ao usuario de diferentes formas
print('A soma dos numero digitados é igual a: {}'.format(soma))
print('A soma entre {} e {} é igual a: {}'.format(numero1,numero2,soma))

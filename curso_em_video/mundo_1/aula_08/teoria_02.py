#Utilizando Módulos
#Importa apenas a função sqrt e floor da biblioteca matemática
from math import sqrt, floor
#Calcula apenas a raiz quadrada do número
numero = int(input('Digite um número: '))
raiz = float(sqrt(numero))
print(f'A raiz do número {numero} é: {floor(raiz)} \n')

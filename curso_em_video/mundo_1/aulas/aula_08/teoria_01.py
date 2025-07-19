#Utilizando Módulos
#Importa toda a biblioteca de matemática
import math
#Manipula um número com funções da biblioteca
numero = int(input('Digite um número: '))
raiz = float(math.sqrt(numero))
print(f'Quanto ao número digitado, podemos ter as seguintes possibilidades: \n'
      f'A raiz de {numero} é:  {math.ceil(raiz)} \n'
      f'O quadrado de {numero} é: {math.pow(numero,2)}')

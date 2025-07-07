#Escreva um programa que converta uma temperatura digitada em ºC para ºF e ºK.
#Pede a temperatura ao usuário
c = float(input('Digite a temperatura em ºC (Celsius): '))
#Converte e exibe a mesma temperatura em Fahrenheit e Kelvin
print(f'A temperatura inserida equivale a: \n'
      f'{((c * 9/5)) + 32 }ºF (Fahrenheit) \n'
      f'{c+ 273.15 }ºK (Kelvin) \n'
      f'{c}ºC (Celsius)')
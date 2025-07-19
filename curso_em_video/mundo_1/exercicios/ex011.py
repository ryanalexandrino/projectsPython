# Faça um programa que leia a largura e altura de uma parede em metros
# Calcule sua área e quantidade de tinta necessária para pinta-la
# Cada litro de tinta pinta uma area de 2M

# Pede as medidas da parede ao usuário
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

# Calcula e exibe a área e quantidade de tinta necessária para pinta-la
print(f'A parede possui uma area de {largura * altura:.1f} metros, sendo necessário {(largura * altura) / 2:.1f} '
      f'litros de tinta para pinta-la por completo')

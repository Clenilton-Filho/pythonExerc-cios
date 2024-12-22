
# Catetos e Hipotenusa

from math import sqrt
from math import pow

catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
hipo = sqrt(catop**2+catad**2)

print(f'O valor da hipotenusa para os dois valores de catetos será de: {hipo:.3f}')

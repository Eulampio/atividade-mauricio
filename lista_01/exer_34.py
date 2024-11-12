
a = float(input("Digite um nº: ")) 
b = float(input("Digite outro nº: ")) 

import math

def hipotenusa(a, b):
    return math.sqrt(a * 2 + b * 2)

print("A hipotenusa de um triângulo retângulo é: ",hipotenusa(a, b))
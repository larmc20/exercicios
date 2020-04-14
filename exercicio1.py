#Escreva um programa que retorne o seno, coseno e a tangente de um ângulo informado.add()

#imports
from math import sin,cos,tan

x = int(input(r"Insira o angulo: "))

seno = sin(x)
coseno = cos(x)
tangente = tan(x)

print(f'O Angulo x = {x}° possui: seno {seno:.2f}, coseno {coseno:.2f}, tangente {tangente:.2f}')
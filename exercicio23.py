#imports
from random import randint
numero = randint(0,9999)

letras = [i for i in str(numero)]

if len(letras) > 3:
    print("Milhares: " + letras[0])
    print("Centenas: " + letras[1])    
    print("Dezenas: " + letras[2])
    print("Unidades: " + letras[3])
elif len(letras) > 2:
    print("Centenas: " + letras[0])    
    print("Dezenas: " + letras[1])
    print("Unidades: " + letras[2])
elif len(letras) > 1:git ps
    print("Dezenas: " + letras[0])
    print("Unidades: " + letras[1]) 
else:
    print("Unidades: " + letras[0]) 


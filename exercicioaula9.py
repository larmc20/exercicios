""" 
1) Crie um programa que leia o nome completo de uma pessoa
e mostre:
a. O nome com todas as letras maíusculas
b. O nome com todas as letras minúsculas
c. Quantas letras existem sem considerar os espaços
d. quantas letras tem o primeiro nome


2) Faça um programa que leia o número de 0 a 9999 e
mostre na tela cada um dos dígitos separados

3) Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com santo

4) Faça um programa que leia uma frase pelo teclado
e mostre:

a. Quantas vezes aparece a letra A
b. Em que posição ela aparece pela primeira e última vez

5) Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o ultimo nome separadamente.add()


"""
#imports
import random


# 1 -
def teste():
    nome = str(input("Insira o nome: "))

    print(nome.upper())
    print(nome.lower())
    print(len(nome.replace(" ","")))
    print(nome.find(" "))

# 2 - 
def teste2():
    return [ letras for letras in str(random.randint(1,9999))]



# 3 - 
def teste3():
    nome = str(input("Insira o nome da cidade: "))
    result = print("há") if "santo" in nome[:nome.find(" ")].lower() else print("Não há") #ternary operator if else

#4 -
def teste4():
    frase = str(input("Insira a frase:\n"))   
    print(frase.lower().count("a"), "\n ------")
    print(frase.find("a"), " ", (~frase.find("a")) + len(frase) + 1, " ", len(frase))
    
teste4()
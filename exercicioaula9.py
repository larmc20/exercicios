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
# 1 -
def teste():
    nome = str(input("Insira o nome: "))

    print(nome.upper())
    print(nome.lower())
    print(len(nome.replace(" ","")))
    print(nome.find(" "))


teste()


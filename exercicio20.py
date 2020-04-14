"""O mesmo professor do desafio 019 quer sortear a ordem de apresentação
 de trabalhos dos alunos. Faça um programa que leia o nome dos quatro 
 alunos e mostre a ordem sorteada."""

 #imports
import random

lista = []

for i in range(1,5):
    lista.append(str(input(f"Coloque o nome do {i}° aluno: ")))
random.shuffle(lista)
print(lista)


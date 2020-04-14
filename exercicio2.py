"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela 
o nome do escolhido."""

#imports
import random

n1 = str(input("Aluno 1:\n"))
n2 = str(input("Aluno 2:\n"))
n3 = str(input("Aluno 3:\n"))
n4 = str(input("Aluno 4:\n"))

alunos = [n1, n2, n3, n4]
print(type(alunos))

print("O aluno escolhido foi {}".format(random.choice(alunos)))


"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela 
o nome do escolhido."""
#imports
import random

def main():
    alunos = []
    for i in range(1,5):
        alunos.append(str(input(f"Aluno {i}:\n")))
    print(type(alunos))

    print("O aluno escolhido foi {}".format(random.choice(alunos)))

if __name__ == "__main__":
    main()
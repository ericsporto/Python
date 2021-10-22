import math, random

# ler um número real pelo teclado e mostrar sua porção inteira:

n = float(input("Digite o número: "))
print("A porçao inteira de {:.5f} é {}".format(n, math.floor(n)))

# ler o comp. do cateto oposto, do adjacente e calcular a hipotenusa de um triângulo retângulo:

cat_op = int(input("Digite o comprimento do cateto oposto: "))
cat_adj = int(input("Digite o comprimento do cateto adjacente: "))
hipot = math.hypot(cat_op, cat_adj)
print("Os catetos digitados foram {:.2f} e {:.2f} e a hipotenusa calculada foi de {:.2f}".format(cat_op, cat_adj, hipot))

# ler um ângulo qualquer e mostrar na tela o valor de seno, cosseno e tangente:

angulo = float(input("Digite o ângulo: "))
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
print("O ângulo escolhido foi {:.2f}".format(angulo))
print("O seno do ângulo escolhido é {:.2f}".format(sen))
print("O cosseno do ângulo escolhido é {:.2f}".format(cos))
print("A tangente do ângulo escolhido é {:.2f}".format(tan))

# faça um programa que ajude um professor a sortear entre seus 4 alunos, um para lhe ajudar, lendo os nomes detodos e depois sorteando um.

a1 = input("Digite o nome: ")
a2 = input("Digite o nome: ")
a3 = input("Digite o nome: ")
a4 = input("Digite o nome: ")
alunos = [a1, a2, a3, a4]
print("Sorteio:")
print("O aluno escolhido foi", random.choice(alunos))

# sortear a ordem de trabalhos dos alunos anteriores. Ler o nome dos alunos e mostrar a ordem sorteada.

al1 = input("Digite o nome: ")
al2 = input("Digite o nome: ")
al3 = input("Digite o nome: ")
al4 = input("Digite o nome: ")
alunos = [al1, al2, al3, al4]
random.shuffle(alunos)
print("A ordem escolhida foi:")
print(alunos)




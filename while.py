# fazer um programa que leia o sexo de uma pessoa mas que só aceite os valores M ou F
# Caso esteja errado, peá uma digitação novamente até obter o valor certo:

sexo = str(input("Por favor, informe o seu sexo: [M/F]")).strip().upper()[0]
while sexo not in "FM":
    sexo = str(input("Resposta incorreta, tente de novo!")).strip().upper()[0]
print("Sexo {} computado!".format(sexo))
print("Podemos preosseguir...")


# fazer um programa onde o computador vai pensar em um número inteiro de 0 a 10
# peça para o usuário tentar descobrir este numero
# mostre se o usuario acertou ou não e quando acertar, quantos palpites foram:

import random
from time import sleep

print("Vamos jogar?.....")
sleep(1) 
print("Estou pensando em um número de 0 a 10. Quer tentar adivinhar?")
sleep(1)

n = int(input("Digite um número de 0 a 10: "))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computer = random.randint(0, 10)
cont = 0
while n not in lista:
    n = int(input("Número inválido! Digite um número de 0 a 10: "))
if n != computer:
    while n != computer:
        cont = cont + 1
        n = int(input("Não foi dessa vez! Você digitou {}.\nTente de novo: ".format(n)))
        if n == computer:
            cont = cont + 1
sleep(1)
print("Parabens! Você acertou! Precisou de {} palpites!!!".format(cont))

# criar um programa que leia dois valores e mostre o menu: (1) somar (2) multiplicar (3) maior
# (4) novos números (5) sair do programa. o programa deverá realizar a solicitação em cada caso.


n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
soma_valores = n1 + n2
multiplicacao = n1 * n2
maior = n1
print("""Suas opções são:
(1) Somar
(2) Multiplicar
(3) Maior valor
(4) Adicionar novos números
(5) Sair""")
escolha = int(input("Escolha uma opção: "))
lista = [1, 2, 3, 4, 5]
while escolha not in lista:
    escolha = int(input("Opção inválida! Escolha uma opção: "))
if escolha == 1:
        print("Os números escolhidos foram {} e {} e sua soma é: {}.".format(n1, n2, soma_valores))
if escolha == 2:
        print("Os números escolhidos foram {} e {} e sua multiplicação é: {}.".format(n1, n2, multiplicacao))
if escolha == 3:
        if n2 > n1:
             maior = n2
        print("Os números escolhidos foram {} e {} e o maior é: {}.".format(n1, n2, maior))
        if n1 == n2:
            print("Os dois valores são exatamente iguais!")
if escolha == 4:
    n11 = float(input("Digite o primeiro novo valor: "))
    n22 = float(input("Digite o segundo novo valor: "))
    soma_valores = n11 + n22
    multiplicacao = n11 * n22
    maior = n11
    print("""Suas opções são:
    (1) Somar
    (2) Multiplicar
    (3) Maior valor
    (4) Adicionar novos números
    (5) Sair""")
    escolha = int(input("Escolha uma opção: "))
    while escolha == 4:
        n11 = float(input("Digite o primeiro valor: "))
        n22 = float(input("Digite o segundo valor: "))
        soma_valores = n11 + n22
        multiplicacao = n11 * n22
        maior = n11
        print("""Suas opções são:
        (1) Somar
        (2) Multiplicar
        (3) Maior valor
        (4) Adicionar novos números
        (5) Sair""")
        escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        print("Os números escolhidos foram {} e {} e sua soma é: {}.".format(n11, n22, soma_valores))
    if escolha == 2:
        print("Os números escolhidos foram {} e {} e sua multiplicação é: {}.".format(n11, n22, multiplicacao))
    if escolha == 3:
        if n22 > n11:
             maior = n22
        print("Os números escolhidos foram {} e {} e o maior é: {}.".format(n11, n22, maior))
        if n1 == n2:
            print("Os dois valores são exatamente iguais!")
    if escolha == 5:
        print("Obrigado por utilizar nossos serviços! Tenha um bom dia!")
if escolha == 5:
    print("Obrigado por utilizar nossos serviços! Tenha um bom dia!")


# faça um programa que leia um número qualquer e mostre o seu fatorial:

from time import sleep
num = int(input("Digite o númeto a ser fatorado: "))
print("Calculando {}!:".format(num))
f = 1
sleep(1)
while num > 0:
    print(" {} ".format(num), end="")
    print("x" if num > 1 else "= ", end=(""))
    f = f * num
    num = num - 1
print("{}".format(f))

#  desenvolver um programa que leia o primeiro termo e a razão de uma PA e mostre os primeiros 10 termos usando while:

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeiro + (10 - 1) * razao
while primeiro < decimo:
    print("{}".format(primeiro + razao), end= "-")
    primeiro = primeiro + razao
print("ACABOU")

# utilizar o exercício anterior e perguntar se o usuário quer mostrar mais termos da PA.
# Só parar quando ele digitar 0

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeiro + (10 - 1) * razao
while primeiro < decimo:
    print("{}".format(primeiro + razao), end="-")
    primeiro = primeiro + razao
print("ACABOU")
print("""\nGostaria de visualizar mais termos?
Para SIM, digite o número de termos.
Para Não, digite 0 (Zero).""")
adicional = int(input("Quantos: "))
if adicional == 0:
    print("Obrigado por utilizar nossos serviços!")
else:
    decimo_novo = primeiro + (adicional - 1) * razao
    while adicional != 0 and primeiro <= decimo_novo:
        print("{}".format(primeiro + razao), end="-")
        primeiro = primeiro + razao
print("ACABOU")

# escreva um programa que leia n inteiro e mostre na tela os n primeiros números de uma sequência de fibonacci

print("-=-"*10)
print("    Sequência de Fibonacci")
print("-=-"*10)
n = int(input("Digite quantos termos: "))
t1 = 0
t2 = 1
print("{} - {} -".format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(" {} -".format(t3), end="")
    cont = cont + 1
print("FIM!")

# crie um programa que leia vários números e que só vai parar quando o usuário digitar 999.
# no final mostre quantos números foram digitados e qual foi a soma entre eles.

number = int(input("Digite seu número: "))
contador = 0
soma = 0 + number
while number != 999:
    number = int(input("Digite mais um número para somar ou 999 para sair: "))
    contador = contador + 1
    if number != 999:
        soma = soma + number
print("Você digitou {} números e a soma entre eles é {}".format(contador, soma))

# criar um programa que leia vários números inteiros e mostre no fianl a média entre todos eles
# e mostre qual foi o maior valor e o menor valor. o Programa deve perguntar ao usuário se
# ele que ou não continuar digitando valores.

resp = "S"
media = contagem = maior = menor = soma = 0
while resp in "Ss":
    valores = int(input("Digite o valor: "))
    soma = soma + valores
    contagem = contagem + 1
    if contagem == 1:
        maior = menor = valores
    else:
        if valores > maior:
             maior = valores
        if valores < menor:
            menor = valores
        
    resp = str(input("Gostaria de digitar um novo valor: [S/N] ")).strip().upper()[0]
media = soma / contagem
print("""A média entre os {} números digitados foi de {:.2f},
o maior valor foi {} e o menor foi {}.""".format(contagem, media, maior, menor))




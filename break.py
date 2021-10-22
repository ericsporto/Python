# crie um programa que leia vários números e que só vai parar quando o usuário digitar 999.
# no final mostre quantos números foram digitados e qual foi a soma entre eles.

c = s = 0
while True:
    num = (int(input("Digite um número (999 para PARAR!): ")))
    if num == 999:
        break
    c = c + 1
    s = s + num
    
print(f"A quantidade de números digitados foi {c} e a soma entre eles é de {s}.")

# crie um programa que mostre a tabuada de vários números, um de cada vez. 
# O programa será interrompido quando o valor digitado for negativo

while True:
    numero = int(input ("Digite o número para ver sua tabuada: "))
    if numero < 0:
        break
    print("-"*30)
    for c in range(1, 11):
        print(f"{numero} x {c} = {numero*c}")
    print("-"*30)
print("Programa Tabuada encerrado! Obrigado")

# fazer um programa que jogue par ou impar com o usuário.
# o jogo só será interrompido quando o jogador perder.
# mostrando o total de vitórias consecutivas que ele conquistou.

import random
from time import sleep
print("-=-"*9)
print("\033[44mVamos jogar Par ou Ímpar?\033[m")
print("-=-"*9)
sleep (2)
resultado_par = "Par"
resultado_impar = "Ímpar"
resultado = soma = cont = 0
vitoria_usu = "Usuario venceu"
vitoria_comp = "Computador venceu"
while True:
    p_ou_i = str(input("\033[33mPar ou Ímpar?[P/I] \033[m")).strip().upper()[0]
    valor = int(input("\033[33mDigite seu valor: \033[m"))
    computer = random.randint(1, 100)
    soma = valor + computer
    cont = cont + 1
    if soma % 2 == 0:
        resultado = resultado_par
    else:
        resultado = resultado_impar
    
    if p_ou_i in "Pp" and resultado_par == resultado or p_ou_i in "Ii" and resultado_impar == resultado:
        vitoria_usu = False
        print(f"Você digitou {valor}, eu escolhi {computer} e a soma é {soma}.")
        print("Parabéns, você VENCEU!!!!")       
    else:
        vitoria_comp = True
        print(f"Você digitou {valor}, eu escolhi {computer} e a soma é {soma}.")
        print(f"Desta vez eu ganhei, mas foram {cont} vitórias consecutivas!!!")
        break

# criar um programa que leia a idade e o sexo de várias pessoas. O programa deve perguntar se o usuário que continuar.
# no final deve ser mostrado: quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e
# quantas mulheres tem menos de 20 anos.

cont_idade = 0
cont_sexo_m = 0
cont_sexo_f = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = " "
    while sexo not in "MmFf":
        sexo = str(input("Digite o sexo: [M/F] ")).strip().upper()[0]
  
    if idade > 18:
        cont_idade=+ 1
    if sexo in "Mm":
        cont_sexo_m =+ 1
    if sexo in "Ff" and idade < 20:
        cont_sexo_f =+ 1

    n = " "    
    while n not in "SsNn":   
        n = str(input("Gostria de cadastrar outra pessoa? [S/N]: ")).strip().upper()[0]
    if n in "Nn":
        print(f"Foram cadastrados {cont_idade} pessoas com mais de 18 anos.")
        print(f"Foram cadastrados {cont_sexo_m} homens.")
        print(f"Foram cadastradas {cont_sexo_f} mulheres com menos de 20 anos.")
        break

# criar um programa que leia o nome e o preço de vários produtos. O programa deve perguntar se o usuário quer continuar.
# ao final, o programa deve mostrar: qual o total gasto na compra, quantos produtos custam mais de R$1000,00
# e qual é o nome do produto mais barato:

soma = mais1000 = cont = menor = 0
barato = " "
while True:
    nome = str(input("Digite o nome do produto: ")).strip()
    preco = float(input('Digite o preço do produto: R$'))
    soma = soma + preco
    cont =+ 1  

    if preco > 1000:
        mais1000 =+ 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    pergunta = " "
    if pergunta not in "SsNn":
        pergunta = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if pergunta in "Nn":
        break

print(f"O valor total gasto foi: R${soma:.2f} .")
print(f"{mais1000} produtos custam mais que R$1000.00")
print(f"{nome} foi o produto mais barato custando R${menor:.2f}.")


#criar um programa que simule o funcionamento de um cx eletrônico. 
# no início perguntar qual o valor a ser sacado(inteiro) e informar qual a quantidade de células
# serÃo entregues levando em consideração que o cx tem as células: 50, 20, 10 e 1.

print("-=-"*20)
print("                CAIXA ELETRÔNICO")
print("-=-"*20)
valor = int(input("Qual o valor deseja sacar? R$"))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${ced} .")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
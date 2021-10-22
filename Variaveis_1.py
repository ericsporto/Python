# fazer um programa onde o computador vai pensar em um número inteiro de 0 a 5
# peça para o usuário tentar descobrir este numero
# mostre se o usuario acertou ou não

import random

print("Vamos jogar? Estou pensando em um número de 0 a 5. Quer tentar adivinhar?")
n = int(input("Digite um número de 0 a 5: "))
lista = [0, 1, 2, 3, 4, 5]
comp = (random.choice(lista))
if n == comp:
    print("Parabéns! Você acertou! Eu escolhi {} e você digitou {}!.".format(comp, n))
elif n > 5:
    print("Opa! O número precisa ser de 0 a 5!")
else:
    print("Não foi desta vez! Eu escolhi {} e você digitou {}! Tente outra vez!".format(comp, n))

# fazer um programa que vai ler a velocidade de um carro.
# se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado
# a multa vai custa R$ 7.00 por Km acima do limite

v = float(input("Velocidade: "))
v_limite = 80
multa = (v - v_limite) * 7
if v > v_limite:
    print("Sua velocidade foi de {}Km/h e você passou do limite de {}Km/h permitido".format(v, v_limite))
    print("Sua multa foi de R${:.2f}.".format(multa))
else:
    print("Você está dentro do limite de {}Km/h permitido e não foi multado!".format(v_limite))

# criar um programa que lê um número inteiro e mostre se ele é par ou impar

numero = int(input("Digite um número: "))
divisao = numero % 2
if divisao == 0:
    print("O número digitado {} é par".format(numero))
else:
    print("O número digitado {} não é par".format(numero))

# criar um prgrama que pergunte a ditância da uma viagem em Km.
# calcular o preço da passagem cobrando R$0.50 por Km até 200Km e 
# R$0.45 por Km para viagens mais longas.

km = float(input("Qual a kilometragem da sua viagem em Km? "))
curta = km * 0.50
longa = km * 0.45
if km <= 200:
    print("O valor da passagem é R${:.2f}".format(curta))
else:
    print("O valor da passagem é R${:.2f}".format(longa))

# fazer um programa que leia um ano qulquer e diga se ele é Bissexto

ano = int(input("Digite um ano: "))
dezena_por_4 = ano % 4
if dezena_por_4 == 0:
    print("O ano de {} é BISSEXTO".format(ano))
else:
    print("O ano de {} NÃO é BISSEXTO".format(ano))

# fazer um programa que leia três número e diga qual é o maior e qual é o menor

n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print("O maior valor digitado foi {}".format(maior))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("O menor valor digitado foi {}".format(menor))

# fazer um programa que pergunte o salário e calcule o seu aumento:
# quem recebe mais de R$1250,00 receberá um aumento de 10%
# para inferiores ou iguais, aumento de 15%

salario = float(input("Digite o seu salário:R$ "))
s_maior = (salario * (10/100)) + salario
s_menor = (salario * (15/100)) + salario
if s_maior > 1250.00:
    print("Seu novo salário com aumento de 10% será de R${:.2f}".format(s_maior))
if s_menor <= 1250.00:
    print("Seu novo salário com aumento de 15% será de R${:.2f}".format(s_menor))


# criar um programa que leia três retas e diga se podem ou não formar um triângulo

reta1 = float(input("Digite o tamanho em metros da primeira reta:"))
reta2 = float(input("Digite o tamanho em metros da segunda reta:"))
reta3 = float(input("Digite o tamanho em metros da terceira reta:"))
condicao = reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2
if condicao == True:
    print("Essas medidas: {}, {} e {} podem formar um triângulo".format(reta1, reta2, reta3))
else:
    print("Essas medidas: {}, {} e {} NÃO podem formar um triângulo".format(reta1, reta2, reta3))

    
# fazer um programa para gerar empréstimos. Perguntar: valor da casa, salário e em quantos anos ele vai pagar.
#calcular o valor da prestação mensal sabendo que ela não pode execer 30% do salário ou então
# será recusado.

v_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o valor do seu salário: R$"))
anos  = int(input("Em quantos anos deseja pagar? "))
prestacao = v_casa / anos
condicao = prestacao < salario * (30/100)
if condicao == True:
    print("\033[1;33mParabéns, Empréstimo Aprovado!\033[m")
    print("O valor das suas parcelas é de R${:.2f}, pagas mensalmente durante {} anos!".format(prestacao, anos))
else:
    print('\033[0;31;40mEmpréstimo Negado!\033[m')
    print("Sua prestação exece o valor de 30% do seu salário!")

# fazer um programa que leia dois números inteiros e compare-os
#mostrar: o primeiro valor é maior, o segundo é maior, os dois são iguais

v1 = int(input("Digite o primeiro valor: "))
v2 = int (input("Digite o segundo valor: "))

if v1 > v2:
    print("O primeiro valor {}, é maior!".format(v1))
elif v2 > v1:
    print("O segundo valor {}, é maior!".format(v2))
elif v2 == v1:
    print("Os valores digitados {} e {}, são iguais!".format(v1, v2))

# fazer um programa qie leia o ano de nascimento de um jovem e diga se ele deve se alistar, se o alistamento já passou 
# e quanto tempo falta para se alistar ou quanto tempo já passou do alistamento

ano_n = int(input("Digite o ano do seu nascimento: "))
ano_atual = 2021
idade = ano_atual - ano_n
if ano_atual - ano_n == 18:
    print("Você nasceu em {} e deve se alistar imediatamente!".format(ano_n))
elif ano_atual - ano_n > 18:
    print("Você nasceu em {} e deveria ter se alistado a {} anos.".format(ano_n, idade))
elif ano_atual - ano_n < 18:
    print("Você nasceu em {} e deve se alistar somente daqui a {} anos.".format(ano_n, idade))

# criar um programa que leia duas notas de um aluno e calcule a média: 
# média abaixo de 5.0: Reprovado
# média entre 5.0 e 6.9: Recuperação
# média em 7.0 ou superior: Aprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Sua média foi {} e você foi \033[32mAPROVADO!\033[m".format(media))
elif media > 5 and media < 6.9:
    print("Sua média foi {} e você está em \033[33mRECUPERAÇÃO!\033[m".format(media))
elif media <= 5:
    print("Sua média foi {} e você foi \033[31mREPROVADO!\033[m".format(media))

# criar um programa que leia o ano de nascimento de um atleta e diga a sua categoria:
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 anos: sênior
# acima: master

nasc = int(input('Digite o seu ano de nascimento: '))
an_at = 2021
id = an_at - nasc
if an_at - nasc < 9:
    print("Você tem {} anos e sua categoria é Mirim!".format(id))
elif an_at - nasc >= 9 and an_at - nasc < 14:
    print("Você tem {} anos e sua categoria é Infantil!".format(id))
elif an_at - nasc >= 14 and an_at - nasc < 19:
    print("Você tem {} anos e sua categoria é Júnior!".format(id))
elif an_at - nasc >= 19 and an_at - nasc <= 20:
    print("Você tem {} anos e sua categoria é Sênior!".format(id))
elif an_at - nasc > 20:
    print("Você tem {} anos e sua categoria é Master!".format(id))

# criar um programa que leia três retas e diga se podem ou não formar um triângulo
# dizer se é equilátero, isosceles ou escaleno

reta1 = float(input("Digite o tamanho em metros da primeira reta:"))
reta2 = float(input("Digite o tamanho em metros da segunda reta:"))
reta3 = float(input("Digite o tamanho em metros da terceira reta:"))
condicao = reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2
equi = reta1 == reta2 == reta3
iso = reta1 == reta2 or reta2 == reta3 or reta3 == reta1
esc = reta1 != reta2 != reta3 != reta1
if condicao == True:
    if equi == True:
        print("Essas medidas: {}, {} e {} podem formar um triângulo Equilátero.".format(reta1, reta2, reta3))
    
    elif iso == True:
        print("Essas medidas: {}, {} e {} podem formar um triângulo Isósceles.".format(reta1, reta2, reta3))
    
    else:
        print("Essas medidas: {}, {} e {} podem formar um triângulo Escaleno".format(reta1, reta2, reta3))
    
    
else:
    print("Essas medidas: {}, {} e {} NÃO podem formar um triângulo".format(reta1, reta2, reta3))

# deselvolver uma lógica que leia peso e altura e calcule o IMC e classifique o usuário:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# de 25 até 30: sobrepeso
# 30 a 40:  obesidade
# acima de 40; obesidade mórbida

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Seu IMC é de {:.2f} e você está abaixo do peso ideal".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu IMC é de {:.2f} e você está no peso ideal".format(imc))
elif imc >= 25 and imc <= 30:
    print("Seu IMC é de {:.2f} e você está acima do peso ideal".format(imc))
elif imc >= 30 and imc < 40:
    print("Seu IMC é de {:.2f}. Cuidado você está com obesidade!".format(imc))
elif imc >= 40:
    print("Seu IMC é de {:.2f}. Procure ajuda! Você tem obesidade mórbida!".format(imc))

# elaborar um programa que calcule o valor de um produto considerando o seu valor e condições de pagamento:
# à vista, dinheiro ou cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x: preço normal
# 3x ou mais: 20% de juros

v = float(input("Digite o valor do produto: R$ "))
print(" 1 - À vista (Cheque ou dinheiro) \n 2 - À vista (Cartão) \n 3 - Duas vezes (Cartão) \n 4 - Três ou mais vezes (Cartão)")
forma = int(input("Escolha a forma de pagamento:  "))
f1 = v - (v * (10 / 100))
f2 = v - (v * (5 / 100))
f3 = v / 2
f4 = v + (v * (20 / 100))

if forma == 1:
    print("O valor R${:.2f} do produto com 10% de desconto, à vista no dinheiro ou cheque é de R${:.2f}.".format(v, f1))
elif forma == 2:
    print("O valor R${:.2f} do produto com 5% de desconto, à vista no cartão é de R${:.2f}.".format(v, f2))
elif forma == 3:
    print("O valor R${:.2f} do produto pode ser dividido em 2x é de R${:.2f} no cartão.".format(v, f3))
elif forma == 4:
     vezes = int(input("Em quantas vezes? "))
     cond = f4 / vezes
     if vezes >= 3 and vezes < 10:
             print("O valor R${:.2f} do produto será dividio em {}x de R${:.2f} no cartão.".format(v, vezes, cond))
     else:
            print("Opção válida somente para 3x ou mais.")
else:
    print("Escolha as opções de 1 a 4. Obrigado")

# crie um programa que faça o computador jogar jokempô com o usuário

import random
print("Que tal jogarmos o famoso JOKENPÔ?????")
print(" 1 - Pedra \n 2 - Papel \n 3 - Tesoura")
esc = int(input("Escolha sua opção: "))
pe = 1
pa = 2
te = 3
lista = [1, 2, 3]
computer = random.randint(lista)
if computer == 1 and esc == 1:
    print("Oh oh! Empatamos! Escolhi Pedra e você também!")
elif computer == 1 and esc == 2:
    print("Ahhhh você venceu! Escolhi Pedra e você Papel!")
elif computer == 1 and esc == 3:
    print("Esta eu venci! Escolhi Pedra e você Tesoura!")
elif computer == 2 and esc == 2:
    print("Oh oh! Empatamos! Escolhi Papel e você também!")
elif computer == 2 and esc == 3:
    print("Ahhhh você venceu! Escolhi Papel e você Tesoura!")
elif computer == 2 and esc == 1:
    print("Esta eu venci! Escolhi Papel e você Pedra!")
elif computer == 3 and esc == 3:
    print("Oh oh! Empatamos! Escolhi Tesoura e você também!")
elif computer == 3 and esc == 1:
    print("Ahhhh você venceu! Escolhi Tesoura e você Pedra!")
elif computer == 3 and esc == 2:
    print("Esta eu venci! Escolhi Tesoura e você Papel")
elif esc >= 4:
    print("Escolha 1, 2 ou 3!")
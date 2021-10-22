# fazer um programa que mostre a contagem regressiva de 10 até 0 com 1s de intervalo:
from time import sleep
print("-=-" * 12)
print("Atenção para a contagem regressiva:")
print("-=-" * 12)
sleep(3)
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print("\033[34mFeliz ano Novo!!!!!\033[m") 

# criar um programa que mostre na tela todos os número pares de 1 até 50:

for c in range(1, 50):
    if c % 2 == 0:
        print(c)

# fazer um programa que calcule a some de todos os números ímpares que são multiplos de 3 no intervalo de 1 a 500:

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print("A soma de todos os {} números é de {}.".format(cont, soma))

# ler um número inteiro e mostrar sua tabuada

o = int(input("Digite um número: "))
for c in range(0, 11):
    print("{} x {} = {}".format(o, c, c*o))

# fazer um programa que leia 6 número inteiros e mostre a soma somente daqueles que forem pares. Se o valor digitado
# for impar, desconsidere-o:

soma = 0
cont = 0
for c in range(0, 6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print("A soma dos {} números pares digitados foi {}".format(cont, soma))

# desenvolver um programa que leia o primeiro termo e a razão de uma PA e mostre os primeiros 10 termos:

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end= "-")
print("ACABOU")

# criar um programa que leia um número inteiro e diga se ele é primo ou não:

tot = 0
num = int(input("Digite um número: "))
for c in range(1, num + 1):
    if num % c == 0:
        tot = tot + 1
print("O número {} foi divisível {} vezes".format(num, tot))
if tot == 2:
    print("E por isso ele é um número primo!")
else:
    print("E por isso ele Não é um número primo!")

# fazer um programa que leia uma frase e diga se ela é um Palíndromo.

print("-=-"*12)
print("    Sua frase é um Palíndromo?")
print("-=-"*12)
from time import sleep
sleep(3)
frase = str(input("Digite a sua frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print("Temos um Palíndromo")
else:
    print("A frase digitada não é um Palíndromo")

# criar um programa que leia 7 anos de nascimento e diga quantos atingiram a maioridade e quantos não:

from datetime import date
atual = date.today().year
totmaior = 0
totamenor = 0
for pess in range(1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu? ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totamenor = totamenor + 1
print("Ao todo tivemos {} pessoas maiores e {} pessoas menores de idade".format(totmaior, totamenor))

# fazer o programa que leia o peso de 5 pessoas e diga no final quais foram os maiores e menores pesos encontrados:

maior =0
menor = 0
for pess in range(1, 6):
    peso = float(input("Digite o peso da {} pessoa: ".format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {} Kg.".format(maior))
print("O menor peso lido foi de {} Kg.".format(menor))


# fazer um programa que leia: nome, idade e sexo de 4 pessoas e diga no final:
# a média de idade do grupo
# nome do homem mais velho
# quantas mulheres tem menos de 20 anos

somaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for pessoa in range(1, 5):
    print("------{} Pessoa------".format(pessoa))
    nomes = str(input(("Nome? "))).strip()
    idades = int(input("Idade? "))
    sexos = str(input("Sexo? [M/F] ")).strip()
    somaidade = somaidade + idades
    if pessoa == 1 and sexos in "Mm":
        maioridadehomem = idades
        nomevelho = nomes
    if sexos in "Mm" and idades > maioridadehomem:
        maioridadehomem = idades
        nomevelho = nomes
    if sexos in "Ff" and totmulher20 < 20:
        totmulher20 = totmulher20 + 1
print("A média de idade do grupo é de {} anos.".format(somaidade/4))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo, {} mulheres com menos de 20 anos.".format(totmulher20))




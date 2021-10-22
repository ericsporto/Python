lanche = ("Pizza","Batata Frita","Refrigerante","Sorvete")

for c in lanche:
    print(f"Comi {c}.")
print("Sou guloso!")

for c in range(0, len(lanche)):
    print(f"Vou comer {lanche[c]} na ordem {c}.")
print("Ficarei cheio!")

for cont, c in enumerate(lanche):
    print(f"Já comi {c} na ordem {cont}.")
print("Matei a fome!")


# sorted = organiza a tupla
#Exemplo:
print(sorted(lanche))

# criar um programa que tenha uma tupla totalmente preenchida por extenso de 0 a 20
# seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso:

tupla = ("zero","um","dois","três", "quatro","cinco","seis",
"sete","oito","nove","dez","onze","doze","treze","quatorze",
"quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if numero >= 0 and numero <= 20:
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o número {tupla[numero]}.")

# criar uma tupla com os 20 primeiros colocados do brasileirão e mostrar:
# a- os 5 primeiros colocados
# b- os 4 últimos colocados
# c- uma lista com os times em ordem alfabetica
# d- em que posição está a chapecoense

tupla = ("Atlético MG","Palmeiras","Fortaleza","Bragantino", "Flamengo","Corinthians","Atlético GO",
"Ceará","Atlético PR","Internacional","Santos","São Paulo","Fluminense","Juventude","Cuiabá",
"Bahia","América MG","Grêmio","Sport","Chapecoense")

print(f"Os 5 primeiros colocados são {tupla[0:5]}.")
print(f"Os últimos 4 colocados são {tupla[16:21]}.")
print(f"Times em ordem alfabética: {sorted(tupla)}.")

for cont, n in enumerate(tupla):
    if n == "Chapecoense":
        print(f"A Chapecoense está neste instante na {cont + 1} posição.")


# criar um programa que gere 5 números aleatórios e colocar dentro de uma tupla.
# depois disso mostrar a listagem de números gerados e indicar o maior e menor valor.

from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Eu sorteei os valores: {n}.")
print(f"O maior valor sorteado foi {max(n)}.")
print(f"O menor valor sorteado foi {min(n)}.")

# criar um programa que leia 4 valores pelo teclado e guarde-os em um tupla. No final mostre:
# quantas vezes apareceu o valor 9
# em que posição foi digitado o primeiro valor 3
# quais foram os número pares

valores = (int(input("Digite um valor: ")),
int(input("Digite outro valor: ")),
int(input("Digite mais um valor: ")),
int(input("Digite o último valor: ")))
   
print(f"Os valores digitados foram: {valores}.")
print(f"O número nove aparece {valores.count(9)} vezes.")

if 3 in valores:
    print(f"O número 3 aparece na {valores.index(3) + 1} posição.")    
else:
    print(f"O número 3 não foi digitado em nenhuma posição.")
   
print(f"Os valores pares digitados foram: ", end="")
for n in valores:
    if n % 2 ==0:
        print(n , end="")

# criar um programa que tenha uma tupla única com nomes de produtos e seus respctivos preços:
# no final, mostrar uma listagem de preços de forma tabular.

produtos = ("Restauração", 100.00,"Extração", 300.00, "Limpeza", 80.00,"Clareamento", 500.00,"Canal", 450.00)

print("="*40)
print("              ODONTOLOGIA")
print("="*40)

for n in range(0, len(produtos)):
    if n % 2 == 0:
        print(f"{produtos[n]:.<30}", end="")
    else:
        print(f"R${produtos[n]:>7.2f}")

# criar um programa que tenha uma tupla com várias palavras
# mostrar para cada palavra, quais as suas vogais

palavras = ("manga","fruta","pereira","odontologia","palavra","miniatura")

for n in palavras:
        print(f"\nNa palavra {n.upper()} existem as vogais: ", end="")
        for letra in n:
            if letra.lower() in "aeiou":
                print(letra, end=" ")
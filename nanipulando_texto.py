# criar um programa que leia o nome completo de uma pessoa e mostre:
# O nome dom todas as letras maiúsculas
# O nome com todas as letras minúsculas
# # Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

frase = input("Digite o seu nome completo: ") 
print(frase)
maiúscula = (frase.upper())
print(maiúscula)
minuscula = (frase.lower())
print(minuscula)
sem_espaco = len(frase.replace(" ",""))
print(sem_espaco)
primeiro = len(frase.split()[0])
print(primeiro)

# fazer um programa que leio de 0 a 9999 e mostre na tela cada um dis dígitos separados
# Unidade, centena, dezena e milhar

frase = input("Digite um número até 4 dígitos: ")
espacos = (frase.replace(""," ").split())
print("Unidade = ", espacos[3])
print("Dezena = ", espacos[2])
print("Centena = ", espacos[1])
print("Milhar = ", espacos[0])

# criar um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"

frase = input("Digite o nome da cidade: ")
print(frase)
lista = (frase.split())
if (lista[0] == "Santo"):
    print("O primeiro nome é Santo")
else:
    print("O primeiro nome não é Santo")

# criar um programa que leia o nome da pessoa e diga se ela tem "Silva" no nome

frase = input("Digite seu nome completo: ")
print(frase)
lista = ("Silva" in frase)
if (lista == True):
    print("Sim, você tem Silva no seu nome!")
else:
    print("Você não tem Silva no nome!")

# fazer um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "a"
# em que posição aparecem a primeira e a última

frase = input("Digite a sua frase: ")
a = (frase.count("a"))
b = (frase.find("a"))
c = (frase.rfind("a"))
print("Quantidade de A encontrado: ", a)
print("O primeiro A aparece na posição: ", b)
print("O último A aparece na posição: ", c)

# fazer um programa que leia o nome de uma pessoa e mostre o primeiro e o último na tela

nome = input("Digite o seu nome: ")
lista = (nome.split())
primeiro_nome = (lista[0])
ultimo_nome = (lista[-1])
print(primeiro_nome)
print(ultimo_nome)


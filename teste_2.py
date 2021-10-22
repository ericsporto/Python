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
lista = [ 0 , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computer = random.randint(0, 10)
cont = 1
while n in lista:
    if n != computer:
            cont = cont + 1
            n = int(input(f"Não foi dessa vez! Você digitou {n}.\nTente de novo: "))

    if n == computer:
        sleep(1)
        print(f"Parabens! Você acertou! Precisou de {cont} palpites!!!")

while n not in lista:
    n = int(input("Número inválido! Digite um número de 0 a 10: "))
    while n in lista:
        if n != computer:
            cont = cont + 1
            n = int(input(f"Não foi dessa vez! Você digitou {n}.\nTente de novo: "))

        if n == computer:
            sleep(1)
            print(f"Parabens! Você acertou! Precisou de {cont} palpites!!!")
            break

            
    
    
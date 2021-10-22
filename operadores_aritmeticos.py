# operadores_aritmeticos_exercicios

#leia um numero inteiro e mostre seu sucessor e antecessor:

n = int(input("Digite um número: "))
print("O número digitado foi {}, seu antecessor é {} e seu sucessor é {}".format(n, n-1, n+1))

#leia um numero e mostre seu dobro, triplo e raiz quadrada:

t = int(input("Digite um número: "))
print("o número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.0f}".format(t, t*2, t*3, t**(1/2)))

#ler duas notas de um aluno e calcular a média:

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
s = nota1 + nota2

print("A soma das notas é {:.2f} e a média é {:.2f}".format(s, s/2))

#ler valor em metros e transformar em centímetros e milímetros:

metros = float(input("Digite o valor em metros: "))
cent = metros * 100
mil = metros * 1000
print("O número digitado foi {:.2f} que equivale a {:.0f} centímetros e {:.0f} milímetros.".format(metros, cent, mil))

#ler um número inteiro e mostrar sua tabuada

o = int(input("Digite um número: "))
zero = o*0
um = o*1
dois = o*2
tres = o*3
quatro = o*4
cinco = o*5
print("{} x 0 = {}".format(o, zero))
print("{} x 1 = {}".format(o, um))
print("{} x 2 = {}".format(o, dois))
print("{} x 3 = {}".format(o, tres))
print("{} x 4 = {}".format(o, quatro))
print("{} x 5 = {}".format(o, cinco))

#ler a quantia de dinheiro e mostrar quantos dólares ela pode comprar 1 dolar = 3,27 reais.

dinheiro = float(input("Quanto dinheiro você tem: R$"))
dolar = dinheiro / 3.27
print("Você pode comprar US{:.2f} dólares.".format(dolar))

# ler largura e altura de uma parede em metros, calcular a área e a quantidade de tinta necessária para pintar 1l linta 2m2

altura = float(input("Digite o valor da altura: "))
largura = float(input("Digite o valor da largura: "))
m2 = largura*altura
print("A área, baseado nas informações é de {:.2f} m2 e serão necessários {:.2f} litros de tinta.".format(m2, m2/2))

#ler o preço de um produto e mostrar seu novo preço com 5% de desconto

preco = float(input("Digite o preço: "))
novo_preco = (preco)-(preco * (5/100))
print("O valor do produto com desconto é de R${:.2f}".format(novo_preco))

#ler um salário e mostrar o valor com 15% de aumento

salario = float(input("Digite o seu salário: R$"))
novo_salario = (salario) + (salario * (15/100))
print("Seu novo salário com aumento é de R${:.2f}".format(novo_salario))







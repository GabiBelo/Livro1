# Escreva um programa que leia dois números. Imprima o resultado da
# multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
# subtração para calcular o resultado. Lembre-se de que podemos entender a mul-
# tiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
# + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

x = int(input("Digite um primeiro número para multiplicar: "))
y = int(input("Digite o segundo número multiplicador: "))
z = []

while True:
    for x in range(len(y)):
        z.append(x)
        print(z)
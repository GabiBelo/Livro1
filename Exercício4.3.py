#Escreva um programa que leia três números e que imprima o maior e o menor.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print(f"O maior número é o {numero1}")
    print(f"O menor número é o {numero3}")
if numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
    print(f"O maior número é o {numero1}")
    print(f"O menor número é o {numero2}")
if numero2 > numero1 and numero2 > numero3 and numero1 > numero3:
    print(f"O maior número é o {numero2}")
    print(f"O menor número é o {numero3}")
if numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
    print(f"O maior número é o {numero2}")
    print(f"O menor número é o {numero1}")
if numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
    print(f"O maior número é o {numero3}")
    print(f"O menor número é o {numero2}")
if numero3 > numero1 and numero3 > numero2 and numero2 > numero1:
    print(f"O maior número é o {numero3}")
    print(f"O menor número é o {numero1}")
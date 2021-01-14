#Escreva um programa que leia dois números e que pergunte qual operação
#você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

numero1 = float(input("Digite um primeiro número: "))
numero2 = float(input("Digite um segundo número: "))
resultado = input("Qual operação báscia deseja realizar: diminuir, somar, multiplicar ou dividir? ").lower()

if resultado == 'diminuir':
    if numero2 >= numero1:
        print(f"O resultado é: {numero2 - numero1}")
    else:
        print(f"O resultado é: {numero1 - numero2}")
elif resultado == 'somar':
    print(f"O resultado é: {numero1 + numero2}")
elif resultado == 'multiplicar':
    print(f"O resultado é: {numero2 * numero1}")
elif resultado == 'dividir':
    if numero2 > numero1:
        print(f"o resultado é: {numero2 / numero1}")
    else:
        print(f"O resultado é: {numero1 / numero2}")
else:
    print("Operação inválida!!!")
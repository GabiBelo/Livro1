# Escreva um programa que pergunte o depósito inicial e a taxa de
# juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.

depositoInicial = float(input("Qual valor do depósito inicial? "))
taxaJuros = float(input("\nQual a taxa de juros? "))
meses = 1
valorSomado = 0

while meses <= 24:
    valorSomado = valorSomado + (depositoInicial * (taxaJuros/100))
    depositoInicial += (depositoInicial * (taxaJuros/100))
    print(f'Valor recebido no {meses} mês é de: {depositoInicial}')
    meses += 1

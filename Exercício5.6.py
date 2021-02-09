# Altere o programa anterior para exibir os resultados no mesmo for-
# mato de uma tabuada: 2x1 = 2, 2x2=4, ...

valor = int(input("Digite um valor para saber a tabuada: "))

x = 1
while x <= 10:
    print(f"O resultado para {x} x {valor} = {x * valor}")
    x += 1
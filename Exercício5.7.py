# Modifique o programa anterior de forma que o usuário também
# digite o início e o fim da tabuada, em vez de começar com 1 e 10.

valor = int(input("Digite um valor para saber o início da tabuada: "))
x = int(input("Digite o valor de fim da tabuada: "))


while valor <= x:
    print(f"O resultado para {x} x {valor} = {x * valor}")
    valor += 1

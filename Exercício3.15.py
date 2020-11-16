cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = float(input("Por quantos anos você fuma? "))

vida = (anos * 365 * cigarros) * 10 / 8760
print(f"A quantidade de dias que perdeu foi de: {vida}")
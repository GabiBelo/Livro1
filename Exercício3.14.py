km = float(input("Quantos quilômentros percorridos? "))
dias = int(input("E por quantos dias? "))

custo_dia = 60 * dias
custo_km = km * 0.15
total = custo_dia + custo_km

print(f"O total a ser pago é R${total}")
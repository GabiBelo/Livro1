dias = int(input("Quantidade de dias: "))
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))

dias_convertido = dias * 24 * 3600
horas_convertido = horas * 3600
minutos_convertido = minutos * 60
total = segundos + dias_convertido + horas_convertido + minutos_convertido

print(f"O valor total é de: {total} segundos")
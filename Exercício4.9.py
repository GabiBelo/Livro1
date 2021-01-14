#Escreva um programa para aprovar o empréstimo bancário para
#compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
#salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
#superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
#casa a comprar dividido pelo número de meses a pagar.

casa = float(input("Qual valor da casa que deseja comprar? "))
salario = float(input("Quanto ganha mensalmente? "))
anos = int(input("Em quantos anos deseja pagar a casa? "))
prestacaoMeses = anos * 12
valorPrestacao = casa / prestacaoMeses

if valorPrestacao >= (0.3 * salario):
    print("Sinto muito, o empréstimo não foi aprovado")
else:
    print("Empréstimo aprovado!!")
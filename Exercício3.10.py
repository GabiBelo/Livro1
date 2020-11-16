salario = float(input("Digite seu atual salário: "))
aumento = float(input("E qual a porcentagem que você gostaria de receber? "))

novo_salario = (aumento/100*salario) + salario
aumento_real = (aumento/100*salario)
print(f"O valor do aumento é R${aumento_real}")
print(f"O valor do salário atualizado é de R${novo_salario}")
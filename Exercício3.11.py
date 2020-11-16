mercadoria = float(input("Qual valor da mercadoria? "))
desconto = float(input("Desconto oferecido: "))

valor_desconto = desconto/100 * mercadoria
novo_valor = mercadoria - (desconto/100 * mercadoria)

print(f"O desconto é de R$ {valor_desconto}")
print(f"O valor total com desconto é R${novo_valor}")
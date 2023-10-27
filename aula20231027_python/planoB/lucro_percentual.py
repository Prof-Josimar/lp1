valor_compra = float(input("Valor da compra : "))
valor_venda  = float(input("Valor da venda : "))

lucro_percentual = (valor_venda - valor_compra) / valor_compra * 100
print(f"Lucro em porcentagem {lucro_percentual:.2f} %")




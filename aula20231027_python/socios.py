SOCIOS = 3
acumulado = 0.0
qtd_vendas = 0
valor_venda = float(input("Digite o valor da venda : "))

while valor_venda != 0.0:
    acumulado = acumulado + valor_venda
    qtd_vendas = qtd_vendas + 1
    valor_socio = acumulado / SOCIOS
    print('Acumulado...............: {:.2f}'.format(acumulado))
    print('Cada sócio recebendo....: {:.2f}'.format(valor_socio))
    print("-"*40)
    valor_venda = float(input("Digite o valor da venda : "))


print("-"*40)
print('Acumulado...............: {:.2f}'.format(acumulado))
print("Total de vendas" ,qtd_vendas)

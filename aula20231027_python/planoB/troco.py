"""
01) Faça uma função que receba um valor que é o valor pago, um segundo valor que é o preço do produto e
# retorne o troco a ser dado.
"""

import locale


def real_br_money_mask(my_value):
    a = "{:,.2f}".format(float(my_value))
    b = a.replace(",", "v")
    c = b.replace(".", ",")
    return c.replace("v", ".")


precoProduto = float((input("Digite o preço da compra ? ")))
valorPago = float((input("Digite o valor com que se paga ? ")))

if precoProduto > valorPago:
    print("Valor para inferior ao preço do produto")
else:
    troco = valorPago - precoProduto
    print("Seu troco : R$ ", real_br_money_mask(troco))
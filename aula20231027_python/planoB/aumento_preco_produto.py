# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input("Informe o preço do produto R$  : "))
desc = preco / 100 * 5

preconovo = preco - (preco / 100 * 5)
print(f"Novo  Preço......: {preconovo:.2f}")
print(f"Valor desconto...: {desc:.2f}")

"""
Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias = int(input("Digite a qtd de dias alugados : "))
km_rodados = int(input("Digite a qtd de km rodados : "))
total = (dias * 60) + (km_rodados * 0.15)
print("Voce pagar é de R$ {:.2f} ".format(total))

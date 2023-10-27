"""
nome = input("Digite seu nome : ")
salarioBruto = float(input("Digite o salario : "))
valorDesconto = salarioBruto * ( 8 / 100)
salarioLiquido = salarioBruto - valorDesconto
print("O desconto foi " , valorDesconto )
print("O salario liquido é " , salarioLiquido)
"""

"""
for i in range(3):
    nome = input("Digite seu nome : ")
    salarioBruto = float(input("Digite o salario : "))
    valorDesconto = salarioBruto * ( 8 / 100)
    salarioLiquido = salarioBruto - valorDesconto
    print("O desconto foi " , valorDesconto )
    print("O salario liquido é " , salarioLiquido)
    print("\n")

print("Fim")    
"""

nome = input("Digite seu nome : ")
while nome != "sair":
    salarioBruto = float(input("Digite o salario : "))
    valorDesconto = salarioBruto * ( 8 / 100)
    salarioLiquido = salarioBruto - valorDesconto
    print("O desconto foi " , valorDesconto )
    print("O salario liquido é " , salarioLiquido)
    print("\n")
    nome = input("Digite seu nome : ")    

print("Fim")    
    
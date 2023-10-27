continuar = "S"
venda = 0.0
while continuar != "N":
    valor = float(input("Valor "))
    venda = venda + valor
    print("Acumulado ",venda)
    print("\n")

    continuar = input("Por favor insira 'S' ou 'N': ").upper()    
#fim while


    

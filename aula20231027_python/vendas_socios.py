numero_socios = int(input("Quantos sócios : "))
cont = 0
venda = 0.0
total = 0.0
comis = 0.0
resp = "S"
while resp == "S":
    venda = float(input("Valor da venda"))
    total = total + venda
    comis = total / numero_socios
    print(f"Cada sócio ganhado :  {comis:.2f}")

    resp = input("Deseja repetir")

    cont += 1

else:
    print("O loop while foi encerrado com sucesso!")


"""
terminal.integrated.profiles.windows
terminal.integrated.default


"""

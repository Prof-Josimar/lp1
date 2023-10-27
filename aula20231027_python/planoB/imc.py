altura = float(input("Digite sua altura em metros: "))

peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura**2

print(imc)

match imc:
    case _ if imc < 16:
        print("Magreza grave")
    case _ if imc < 17:
        print("Magreza moderada")
    case _ if imc < 18.5:
        print("Magreza leve")
    case _ if imc < 25:
        print("Saudável")
    case _ if imc < 30:
        print("Sobrepeso")
    case _ if imc < 35:
        print("Obesidade Grau I")
    case _ if imc < 40:
        print("Obesidade Grau II (severa)")
    case _ if imc >= 40:
        print("Obesidade Grau III (mórbida)")
    case _:
        print("Valores inváldos")
        
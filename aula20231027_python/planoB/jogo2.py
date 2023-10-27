import random

REP = 5
numero = random.randint(1, 10)
tentativa = 1

print('******************************')
print('* Jogo da adivinhação *')
print('******************************')

chute = int(
    input(f"Digite um numero entre 1 e 10  (tentativa {tentativa}) de {REP} :  "))


while tentativa < REP:
    if chute == numero:
        print(f"Você acertou na {tentativa} tentativa")
        break
    else:
        if chute < numero:
            print("Você errou! seu chute é menor")
        else:
            print("Você errou! seu chute é maior")
            chute = int(input(f"Digite um numero entre 1 e 10  (tentativa {tentativa}) de {REP} :  "))
    tentativa += 1
print("O número é ", numero)

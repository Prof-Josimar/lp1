import random


chute = int(input("Digite um numero entre 1 e 10 : "))

numero = random.randint(1, 10)
if chute == numero:
    print("Você acertou ")
else:
    print("Você errou! o numero era  ",numero)

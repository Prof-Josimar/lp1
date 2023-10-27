from heapq import merge

mail = "ceatseeduc@gmail.com"
posicao = mail.find("@")

nome = mail[:posicao]
servidor = mail[posicao + 1 :]

print(nome)
print(servidor)

print(mail.center(20, "#"))


for number in range(65, 90):
    print(chr(number), end=" ")

print("\n")

nome = input("Digite seu nome ")
for i in nome:
    print(ord(i))

print("\n")


a = [1, 2, 3, 4]
b = [1, 3, 4, 5, 6, 7]
c = [3, 6, 8, 9, 10]

print(list(merge(a, b, c)))

lst = list(merge(a, b, c))

test_list = list(set(lst))

print("A lista após remover duplicatas : " + str(test_list))



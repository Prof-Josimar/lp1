def adicao(*args):
    resultado = 0

    for argumento in args:
        resultado += argumento
    return resultado

print(adicao(1, 2))
print(adicao(1, 2, 4, 6))
print(adicao(1, 2, 4, 6, 8, 10))


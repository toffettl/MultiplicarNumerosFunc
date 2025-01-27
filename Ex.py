def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)

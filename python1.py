def suma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)

entrada = [1, 2, 3, 4, 5, 6]
print(suma_pares(entrada))
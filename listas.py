#                               # Listas

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[1])
print(numeros[:7+1])
print(numeros[0:4])

numeros = numeros + [11, 12, 12, 14, 15, 16, 17, 18, 19, 20]
print(numeros)
numeros[12] = 13
print(numeros)

#                       # ADICIONAR ITENS AO FINAL DA LISTA COM MÉTODO APPEND

numeros.append(21)
print(numeros)

numeros.append(11 * 2)
print(numeros)
print(len(numeros))

numeros[:10] = ['um', 'dois', 'tres', 'quatro']
print(numeros)
print(len(numeros))

numeros[:] = []
print(numeros)

#                                 # Listas dentro de listas

numeros2 = [23, 24, 25, 26, 27, 28, 29]
numeros3 = numeros2 * 2

numeros4 = [numeros, numeros2, numeros3]
print(numeros4)
print(numeros4[2][4])


a, b = 0, 1
while a < 1000:
    print(a, end=' ')
    a, b = b, a+b

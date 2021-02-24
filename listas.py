squares = [1, 2, 3, 4, 5]

print(squares[0])
print(squares[-1])
print(squares[-1:])
print(squares[:])

squares = squares + [6, 7, 8, 9, 10]

print(squares[:])

squares[9] = 11
print(squares)

# Método Append

numero = int(input('Digite um numero: '))
squares.append(numero)

print(squares);


# fatiamento com Listas

letras = ['a', 'b', 'c', 'd']

print(letras[0:2])

letras[2:3] = ['C', 'D']
print(letras)

# Método len

print(len(letras))
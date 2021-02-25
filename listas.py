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


# Método append

letras.append('F')

# Append com valor digitado pelo usuário 

letra = input('Digite algo para colocar no array')
letras.append(letra)
print(letras)

# Listas dentro de listas

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

print(c)

# estrutura de repetição

a, b = 0, 1
while a < 1000: 
  print(a, end=",")
  a, b = b, a+b

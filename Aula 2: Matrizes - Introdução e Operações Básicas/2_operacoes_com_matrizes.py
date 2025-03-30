import numpy as np

# Matrizes A e B (com dimensões adequadas)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[2, 1], [1, 2]])

# Adição
soma = A + B
print('Adição:\n', soma)

# Subtração
subtracao = A - B
print('Subtração:\n', subtracao)

# Multiplicação por escalar
escalar = 2
multiplicacao_escalar = escalar * A
print('Multiplicação por escalar:\n', multiplicacao_escalar)

# Multiplicação de matrizes
multiplicacao_matrizes = np.dot(A, C) # ou A @ C
print('Multiplicação de matrizes:\n', multiplicacao_matrizes)

import numpy as np

# Operações com vetores

# 1. Adição de Vetores: v + u = [ v1 + u1, v2 + u2, v3 + u3, ..., vn + un ]
# Exemplo: [ 1, 2, 3 ] + [ 4, 5, 6 ] = [ 1 + 4, 2 + 5, 3 + 6 ] = [ 5, 7, 9 ]

# 2. Subtração de Vetores: v - u = [ v1 - u1, v2 - u2, v3 - u3, ..., vn - un ]
# Exemplo: [ 4, 5, 6 ] - [ 1, 2, 3 ] = [ 4 - 1, 5 - 2, 6 - 3 ] = [ 3, 3, 3 ]

# 3. Multiplicação por Escalar: c * v = [ c * v1, c * v2, c * v3, ..., c * vn ]
# Exemplo: 2 * [ 1, 2, 3 ] = [ 2 * 1, 2 * 2, 2 * 3 ] = [ 2, 4, 6 ]

# Vetores
u = np.array([1, 2, 3])
v = np.array([4, -1, 2])

# Adição
soma = u + v
print("Soma:", soma)

# Subtração
subtracao = u - v
print("Subtração:", subtracao)

# Multiplicação por escalar
escalar = 2
multiplicacao = escalar * v
print("Multiplicação por escalar:", multiplicacao)

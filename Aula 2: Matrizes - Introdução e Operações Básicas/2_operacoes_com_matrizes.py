import numpy as np

# Operações com matrizes
# 1. Adição de Matrizes: A + B = [ a11 + b11, a12 + b12, ..., a1n + b1n ] [ a21 + b21, a22 + b22, ..., a2n + b2n ] [ ... ] [ am1 + bm1, am2 + bm2, ..., amn + bmn ]
# Exemplo: [ 1, 2 ] [ 3, 4 ] + [ 5, 6 ] [ 7, 8 ] = [ 1 + 5, 2 + 6 ] [ 3 + 7, 4 + 8 ] = [ 6, 8 ] [ 10, 12 ]

# 2. Subtração de Matrizes: A - B = [ a11 - b11, a12 - b12, ..., a1n - b1n ] [ a21 - b21, a22 - b22, ..., a2n - b2n ] [ ... ] [ am1 - bm1, am2 - bm2, ..., amn - bmn ]
# Exemplo: [ 5, 6 ] [ 7, 8 ] - [ 1, 2 ] [ 3, 4 ] = [ 5 - 1, 6 - 2 ] [ 7 - 3, 8 - 4 ] = [ 4, 4 ] [ 4, 4 ]

# 3. Multiplicação por Escalar: c * A = [ c * a11, c * a12, ..., c * a1n ] [ c * a21, c * a22, ..., c * a2n ] [ ... ] [ c * am1, c * am2, ..., c * amn ]
# Exemplo: 2 * [ 1, 2 ] [ 3, 4 ] = [ 2 * 1, 2 * 2 ] [ 2 * 3, 2 * 4 ] = [ 2, 4 ] [ 6, 8 ]

# 4. Multiplicação de Matrizes: A * B = [ c11, c12, ..., c1p ] [ c21, c22, ..., c2p ] [ ... ] [ cm1, cm2, ..., cmp ] onde cij = sum(ai1 * b1j + ai2 * b2j + ... + ain * bnj)
# Exemplo: [ 1, 2 ] [ 3, 4 ] * [ 5, 6 ] [ 7, 8 ] = [ (1*5 + 2*7), (1*6 + 2*8) ] [ (3*5 + 4*7), (3*6 + 4*8) ] = [ 19, 22 ] [ 43, 50 ]
# quando a maltiplicação de matrizes é possível? quando o número de colunas da primeira matriz é igual ao número de linhas da segunda matriz.
# o resultado C da multiplicação de uma matriz (m x n) por outra matriz (n x p) é uma nova matriz (m x p).
# cada elemento cij é calculado como o produto escalar entre a i-ésima linha da primeira matriz e a j-ésima coluna da segunda matriz. 
# notação: cij = ai1 * b1j + ai2 * b2j + ... + ain * bnj
# Exemplo: A (2x3) * B (3x2) = C (2x2)
# Exemplo: c12 = a11 * b12 + a12 * b22 + a13 * b32
# https://www.youtube.com/watch?v=KKCmjnU2y3o

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
# A * C é outro tipo de multiplicação (element-wise).
print('Multiplicação de matrizes:\n', multiplicacao_matrizes)

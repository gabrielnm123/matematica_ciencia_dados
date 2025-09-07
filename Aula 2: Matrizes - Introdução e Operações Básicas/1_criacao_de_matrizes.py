import numpy as np

# O que é Matrixs?
# Uma matriz é uma organização retangular de números, símbolos ou expressões, dispostos em linhas e colunas.

# Representação de Matrizes
# 1. Notação de Linhas e Colunas: A = [ a11, a12, a13, ..., a1n ] [ a21, a22, a23, ..., a2n ] [ ... ] [ am1, am2, am3, ..., amn ]
# Exemplo: A = [ 1, 2, 3 ] [ 4, 5, 6 ]

# 2. Notação de Índices: A = [ a_ij ] onde 'i' representa a linha e 'j' representa a coluna.
# Exemplo: A = [ a_11, a_12, a_13 ]
#               [ a_21, a_22, a_23 ]
#               [ a_31, a_32, a_33 ]

# Matriz 2x3
A = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz A:\n", A)

# Matriz 2x2
B = np.array([[7, 8], [9, 10]])
print("Matriz B:\n", B)

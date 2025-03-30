import numpy as np

# crie duas matrizes X (2x3) e Y (3x2).
# calcule: X * Y
# crie uma matriz Z (2x2) e calcule: 2 * Z.
# imprima os resultados na tela e compare as dimensões das matrizes resultantes.

X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([[7, 8], [9, 10], [11, 12]])

multiplicacao_matrizes = np.dot(X, Y)
print('Multiplicação de matrizes X e Y:\n', multiplicacao_matrizes)

# multiplicação de matrizes são mais complexas que multiplicação por escalar
# 1. a matriz multiplicante deve ter o mesmo número de colunas que a matriz multiplicada tem de linhas.
# 2. a matriz resultante terá o mesmo número de linhas da matriz multiplicante e o mesmo número de colunas da matriz multiplicada.
# 3. cij = ai1*b1j + ai2*b2j + ... + ain*bnj

# Explore mais operações com matrizes no numpy (transposta, inversa).

import numpy as np

# vetores é uma objeto que possui magnitude e direção

# Representação de vetores

# 1. Notação Coluna: v = [ v1 ] [ v2 ] [ v3 ] [ ... ] [ vn ]
# Exemplo: v = [ 1 ] [ 2 ] [ 3 ]

# 2. Notação Linha: v = [ v1, v2, v3, ..., vn ]
# Exemplo: v = [ 1, 2, 3 ]

# Vetor linha
v = np.array([1, 2, 3])
print('_____Vetor linha com array([1, 2, 3])_____')
print(v)

# Vetor coluna (transporto do vetor linha)
v_coluna = v.reshape(-1, 1)
print('_____Vetor coluna com reshape(-1, 1)_____')
print(v_coluna)
print('_____________________________')  
print(np.array([[1], [2], [3]]), '\n', '_____________________________')

print(v_coluna == np.array([[1], [2], [3]])) # True
print(np.array([[2, 1], [2, 'a'], [3, True]])) # True
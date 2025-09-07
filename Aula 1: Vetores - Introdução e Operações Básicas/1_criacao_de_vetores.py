import numpy as np

# vetores é uma objeto que possui magnitude e direção

# Representação de vetores

# 1. Notação Coluna: v = [ v1 ] [ v2 ] [ v3 ] [ ... ] [ vn ]
# Exemplo: v = [ 1 ] [ 2 ] [ 3 ]

# 2. Notação Linha: v = [ v1, v2, v3, ..., vn ]
# Exemplo: v = [ 1, 2, 3 ]

# Vetor linha
v = np.array([1, 2, 3])
print("Vetor linha:", v)

# Vetor coluna (transporto do vetor linha)
v_coluna = v.reshape(-1, 1)
print("Vetor coluna:", v_coluna)


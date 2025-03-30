import numpy as np

# Vetor linha
v = np.array([1, 2, 3])
print("Vetor linha:", v)

# Vetor coluna (transporto do vetor linha)
v_coluna = v.reshape(-1, 1)
print("Vetor coluna:", v_coluna)

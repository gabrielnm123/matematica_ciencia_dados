import numpy as np

#  Matriz Identidade
I = np.eye(3)
print('Matriz Identidade:\n', I)

# Matriz Zero
Z = np.zeros((2, 2))
print('Matriz Zero:\n', Z)

# Matriz Diagonal
D = np.diag([2, 5, -1])
print('Matriz Diagonal:\n', D)

# Transposta
A = np.array([[1, 2, 3], [4, 5, 6]])
AT = A.T
print('Matriz A:\n', A)
print('Transposta de A:\n', AT)

# Matriz Inversa (se existir)
A = np.array([[4, 2], [3, 1]]) # Matriz invertível
A_inv = np.linalg.inv(A)
print('Matriz A:\n', A)
print('Inversa de A:\n', A_inv)

# Produto Escalar
u = np.array([1, 2, 3])
v = np.array([4, -1, 2])
produto_escalar = np.dot(u, v) # ou u @ v
print('Vetor u:\n', u)
print('Vetor v:\n', v)
print('Produto Escalar de u e v:\n', produto_escalar)
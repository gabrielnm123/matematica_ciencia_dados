import numpy as np

# crie uma matriz B (3x3) qualquer.
# calcule a transposta de B.
# verifique se a matriz B (utilize a que criou no exercício anterior, caso não seja invertível crie outra) tem inversa, e se tiver calcule-a.
# crie dois vetores p e q (com a mesma quantidade de elementos) de sua escolha e calcule o produto escalar entre eles.
# mostre os resultados na tela.

# Matriz 3x3
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'B:\n{B}\n')

# Transposta de B
B_transpose = B.transpose() # ou B.T
print(f'B transposta:\n{B_transpose}\n')

# Verifica se B é invertível
try:
    B_inv = np.linalg.inv(B)
    print(f'Inversa de B:\n{B_inv}\n')
except:
    print('B não é invertível.\n')

# Vetores p e q
p = np.array([1, 2, 3])
q = np.array([4, 5, 6])
print(f'p:\n{p}\n')
print(f'q:\n{q}\n')

# Produto escalar entre p e q
produto_escalar = np.dot(p, q) # ou p @ q
print(f'Produto escalar entre p e q:\n{produto_escalar}\n')

# explore mais funções de álgebra linear no numpy.linalg
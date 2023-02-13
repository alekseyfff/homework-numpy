import numpy as np

N = int(input("Введите N: "))
x = np.arange((N-1), -1, -1)
print(x)

y = np.diag(np.arange(N, -1, -1), k=0)
print(y)
print(np.sum(y.ravel()))

a = ([4, 2, 1], [1, 3, 0], [0, 5, 4])
b = ([4, 12, -3])
result = np.linalg.solve(a, b)
print(result)


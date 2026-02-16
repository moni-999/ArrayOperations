import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])   # 3x2 matrix

# Transpose of A → 2x3
A_T = A.T

B = np.array([[1, 2],
              [3, 4],
              [5, 6]])   # 3x2 matrix

# Dot product (2x3) × (3x2)
result = np.dot(A_T, B)

print("Original Matrix A:")
print(A)

print("Transpose of A:")
print(A_T)

print("Matrix B:")
print(B)

print("Dot Product Result:")
print(result)
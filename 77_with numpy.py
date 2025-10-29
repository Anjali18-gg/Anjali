import numpy as np

# Define two 3x3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Perform operations
add = A + B
sub = A - B
mul = A @ B          # or np.dot(A, B)
transpose_A = A.T

# Display results
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nAddition:\n", add)
print("\nSubtraction:\n", sub)
print("\nMultiplication:\n", mul)
print("\nTranspose of A:\n", transpose_A)

import numpy as np
import numpy.linalg as la

# Builds a matrix from the bits provided.
# Matrix will follow the form noted in the book.
def matrixify(bits, m):
    mat_list = []
    for i in range(0,m):
        mat_list.append([bits[b] for b in range(i,i+m)])
    return np.matrix(mat_list)

full_bits = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1,
    0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0,
    1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1,
    1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0]

det_list = [0]*18

# Creates a list of determinants from several sizes of matrices
for i in range(2, 20):
    mat = matrixify(full_bits, i)
    det_list[i-2] = round(la.det(mat))%2

# Finds the last matrix size that had a determinant of 1
index_last = len(det_list) - 1 - det_list[::-1].index(1) + 2

# Recreate the matrix
mat = matrixify(full_bits, index_last)
# Create the solution vector
arr = np.array([full_bits[i] for i in range(index_last+1, 2*index_last+1)])

# Print the solved matrix equation
print(la.solve(mat, arr) % 2)

import auxiliary as aux
import numpy as np
import numpy.linalg as la

# Builds a matrix from the bits provided.
# Matrix will follow the form noted in the book.
def matrixify(bits, m):
    mat_list = []
    for i in range(0,m):
        mat_list.append(bits[i:i+m])
    return np.matrix(mat_list)


def lsfr_generate(initial_values, initial_n, coeffs, n):
    v = initial_values.copy() + [0]*(n-len(initial_values))
    for i in range(0, n-len(initial_values)):
        v[initial_n+i] = sum([v[m+i] * coeffs[m] for m in range(0,len(coeffs))]) % 2
    return v


def lsfr_attack(v):
    det_list = [0]*18
    # Creates a list of determinants from several sizes of matrices
    for i in range(2, 20):
        mat = matrixify(v, i)
        det_list[i-2] = round(la.det(mat))%2
    # Finds the last matrix size that had a determinant of 1
    index_last = len(det_list) - 1 - det_list[::-1].index(1) + 2
    # Recreate the matrix
    mat = matrixify(v, index_last)
    # Create the solution vector
    arr = np.array(v[index_last+1:2*index_last+1])
    # Print the solved matrix equation
    return (la.solve(mat, arr) % 2).tolist()


if __name__ == "__main__":
    f = open("lsfr_test.txt", 'r')
    m_s = f.read().strip()
    f.close()
    v = [int(m) for m in m_s]
    print(v)
    coeffs = lsfr_attack(v)
    print(coeffs)

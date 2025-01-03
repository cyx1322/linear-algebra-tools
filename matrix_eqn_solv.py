import rref
import linear_solver

def soln_matrix_eqn(matrix, vector_b):
    m = len(matrix)
    n = len(matrix[0]) + 1
    aug_matrix = [[matrix[i][j] for j in range(n-1)] + [vector_b[i]] for i in range(m)]
    aug_rref = rref.reduced_row_echelon_form(aug_matrix, m, n)
    soln = linear_solver.solution_of(aug_rref)[1]
    return soln

if __name__ == "__main__":
    m, n = list(map(int, input("Please input the matrix size m and n: ").split()))
    matrix = rref.input_matrix(m, n)
    vector_b = list(map(float, input("Please enter the targeted vector b: ").split()))
    print(soln_matrix_eqn(matrix, vector_b))
import rref
from rref import is_zero
def solution_of(rref_A: list[list[float]]):
    # The size of the row reduced echelon form (RREF) matrix
    m = len(rref_A)
    n = len(rref_A[0])

    # Determine the consistency of linear system
    for i in range(m - 1, -1, -1):
        if not is_zero(rref_A[i][n-1]):
            # Determine if a nonzero entry is a leading 1
            if is_zero(rref_A[i][n-1] - 1) and is_zero(rref_A[i][:n-1]):
                return None, None
            break

    soln = list([f"x{i}"] for i in range(1, n))
    free_variables = []
    # Solve each variable using RREF
    for j in range(n - 2, -1, -1):
        for i in range(m - 1, -1, -1):
            # A pivot position in the non-augmented column indicates a solution for the variable.
            if is_zero(rref_A[i][j] - 1) and is_zero(rref_A[i][:j]):
                # Empty the variable name, and substitute using value or other variables.
                soln[j] = [rref_A[i][n-1]]
                for column in range(n-2, j, -1):
                    # If a free variable exist, then add it to the result
                    if not is_zero(rref_A[i][column]):
                        soln[j].append(-rref_A[i][column])
                        soln[j].append(soln[column][0])
                break
        else:
            # If no pivot position in that column, then the corresponding variable is a free var
            free_variables.append(soln[j][0])

    # Express the output using a linear combination of vectors.
    formated = {"constant": [0.00 for _ in range(n-1)]}
    for x in free_variables:
        formated[x] = [0.00 for _ in range(n-1)]

    for i in range(n-1):
        firstValue = soln[i][0]

        # If a free variable
        if type(firstValue) == str:
            formated[firstValue][i] = 1.0
            continue

        # If a variable is expressed using free variables and constants
        formated["constant"][i] = firstValue # Add the constants to the constant vector
        for j in range(1, len(soln[i]), 2):
            # For each free variable used, add the coefficient to the corresponding vector
            variable_name = soln[i][j+1]
            formated[variable_name][i] = soln[i][j]
    return soln, formated

if __name__ == "__main__":
    m, n = list(map(int,input().split()))
    matrix_A = rref.input_matrix(m, n)
    rref_A = rref.reduced_row_echelon_form(matrix_A, m, n)
    print(solution_of(rref_A)[1])
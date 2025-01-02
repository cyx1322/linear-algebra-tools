def is_zero(x):
    ## Determine whether a float x is zero
    if type(x) == float:
        return abs(x) < 1e-7
    ## Determine whether a vector, or matrix x is zero matrix
    if type(x) == list:
        for i in x:
            if not is_zero(i):
                return False
        return True
def input_matrix(m, n):
    matrix = []
    for i in range(m):
        matrix.append([])
        entries = list(map(float,input().split()))
        for entry in entries:
            matrix[i].append(entry)
    return matrix

def first_nonzero_column(matrix, m, n, row_bound, col_bound):
    for j in range(col_bound, n):
        for i in range(row_bound, m):
            if not is_zero(matrix[i][j]):
                return j
    return -1

def row_interchanged(matrix, m, n, firstNonzeroColumn, boundary):
    if not is_zero(matrix[boundary][firstNonzeroColumn]):
        return matrix
    for i in range(boundary + 1, m):
        if not is_zero(matrix[i][firstNonzeroColumn]):
            matrix[boundary], matrix[i] = matrix[i], matrix[boundary]
            return matrix
        
def below_eliminated(matrix, m, n, firstNonzeroColumn, boundary):
    for i in range(boundary+1, m):
        if not is_zero(matrix[i][firstNonzeroColumn]):
            scalar = - matrix[i][firstNonzeroColumn] / matrix[boundary][firstNonzeroColumn]
            matrix[i] = [matrix[i][j] + matrix[boundary][j] * scalar for j in range(n)]
    return matrix

def pivot_column(matrix, m, n, row):
    for j in range(n):
        if is_zero(matrix[row][j] - 1):
            return j
    return -1

def above_eliminated(matrix, m, n, pivotColumn, boundary):
    if pivotColumn != -1:
        for i in range(boundary-1, -1, -1):
            if not is_zero(matrix[i][pivotColumn]):
                scalar = - matrix[i][pivotColumn] / matrix[boundary][pivotColumn]
                matrix[i] = [matrix[i][j] + matrix[boundary][j] * scalar for j in range(n)]
    return matrix
def reduced_row_echelon_form(matrix, m, n):
    i, j = 0, 0
    firstNonzeroColumn = first_nonzero_column(matrix, m, n, i, j)
    while firstNonzeroColumn != -1:
        matrix = row_interchanged(matrix, m, n, firstNonzeroColumn, i)
        leading_entry = matrix[i][firstNonzeroColumn]
        if not is_zero(leading_entry - 1):
            matrix[i] = [matrix[i][r]/leading_entry for r in range(n)]
        matrix = below_eliminated(matrix, m, n, firstNonzeroColumn, i)
        i += 1 
        j += 1
        firstNonzeroColumn = first_nonzero_column(matrix, m, n, i, j)
    for i in range(m-1, 0, -1):
        pivotColumn = pivot_column(matrix, m, n, i)
        matrix = above_eliminated(matrix, m, n, pivotColumn, i)
    return matrix

if __name__ == "__main__":
    m, n = list(map(int,input().split()))
    matrix = input_matrix(m, n)
    rref = reduced_row_echelon_form(matrix, m, n)
    
    formatted_result = [[format(0, ".2f") if x==0 else format(x, '.2f') for x in row] for row in rref]
    for i in formatted_result:
        for j in i:
            print(j, end = " ")
        print()
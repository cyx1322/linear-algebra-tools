def is_zero(x):
    ## Determine whether a float x is zero
    if type(x) == float:
        return abs(x) < 1e-7
    ## Determine whether a vector, or matrix x is zero matrix
    if type(x) == list:
        for i in x:
            # If any of the items is nonzero, then the whole matrix is nonzero
            if not is_zero(i):
                return False
        # If all of them are zero, then the matrix itself is zero matrix
        return True


def input_matrix(m, n):
    # Input a mxn matrix
    matrix = []

    for i in range(m):
        matrix.append([])
        entries = list(map(float,input().split()))
        for entry in entries:
            matrix[i].append(entry)
    return matrix

def first_nonzero_column(matrix, m, n, row_bound, col_bound):
    # Find the first nonzero column of a matrix, or a part of a matrix
    for j in range(col_bound, n):
        for i in range(row_bound, m):
            # If any item in a column is nonzero, then it's a nonzero column
            if not is_zero(matrix[i][j]):
                return j
    # If all of the columns are zero, then return -1
    return -1

def row_interchanged(matrix, m, n, firstNonzeroColumn, boundary):
    # Check whether a interchange of rows is needed, and perform an interchange if needed.
    if not is_zero(matrix[boundary][firstNonzeroColumn]):
        # If in the first nonzero column, the first entry is nonzero, then interchange is not needed.
        return matrix
    for i in range(boundary + 1, m):
        # Find the first row in which the entry in the nonzero column is nonzero, this will be used for interchange.
        if not is_zero(matrix[i][firstNonzeroColumn]):
            matrix[boundary], matrix[i] = matrix[i], matrix[boundary]
            return matrix
        
def below_eliminated(matrix, m, n, firstNonzeroColumn, boundary):
    # Eliminate all nonzero entries below a leading 1.
    for i in range(boundary+1, m):
        # If an entry is nonzero
        if not is_zero(matrix[i][firstNonzeroColumn]):
            # Calculate a scalar that makes the entry zero
            scalar = - matrix[i][firstNonzeroColumn] / matrix[boundary][firstNonzeroColumn]
            # Perform the Elementary Row Operation - Replacement
            matrix[i] = [matrix[i][j] + matrix[boundary][j] * scalar for j in range(n)]
    return matrix

def pivot_column(matrix, m, n, row):
    # Find the pivot column
    for j in range(n):
        # Find the leading 1 in a row
        if is_zero(matrix[row][j] - 1):
            return j
    # If no leading 1, then no pivot column in that row
    return -1

def above_eliminated(matrix, m, n, pivotColumn, boundary):
    # Eliminate all nonzero entries above a leading 1
    if pivotColumn != -1:
        # If there's a leading 1 in the row, then eliminate all entries above
        for i in range(boundary-1, -1, -1):
            if not is_zero(matrix[i][pivotColumn]):
                scalar = - matrix[i][pivotColumn] / matrix[boundary][pivotColumn]
                matrix[i] = [matrix[i][j] + matrix[boundary][j] * scalar for j in range(n)]
    return matrix
def reduced_row_echelon_form(matrix, m, n):
    i, j = 0, 0
    firstNonzeroColumn = first_nonzero_column(matrix, m, n, i, j)
    while firstNonzeroColumn != -1:
        # Perform Row Interchange if needed
        matrix = row_interchanged(matrix, m, n, firstNonzeroColumn, i)

        # Store the first entry in the first nonzero column, and normalize it (if needed).
        leading_entry = matrix[i][firstNonzeroColumn]
        if not is_zero(leading_entry - 1):
            matrix[i] = [matrix[i][r]/leading_entry for r in range(n)]
        
        # Eliminate all nonzero entries below the leading 1
        matrix = below_eliminated(matrix, m, n, firstNonzeroColumn, i)

        # Prepare for the next iteration by moving to the next row and column, and finding the next nonzero column.
        i += 1 
        j += 1
        firstNonzeroColumn = first_nonzero_column(matrix, m, n, i, j)

    for i in range(m-1, 0, -1):
        # From the last row, eliminate all nonzero entries above pivot positions
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
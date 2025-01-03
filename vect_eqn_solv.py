import linear_solver
import rref
def soln_vect_eqn(*vectors):
    # Solve a vector equation and return a series of weights (in either explicit form or parametric form). Return None if a solution doesn't exist.
    
    # The size of corresponding augmented matrix
    m, n = len(vectors[0]), len(vectors)
    # Convert the vectors to a augmented matrix
    aug_matrix = [[vectors[j][i] for j in range(n)] for i in range(m)]
    rref_aug = rref.reduced_row_echelon_form(aug_matrix, m, n)
    soln = linear_solver.solution_of(rref_aug)[0]

    return soln

if __name__ == "__main__":
    n = int(input("Please input the number of vectors in the span: "))
    vectors = []
    for i in range(n):
        vector = list(map(float, input(f"Please input the {i+1}th vector (different entries should be seperated by a space): ").split()))
        vectors.append(vector)
    vector_b = list(map(float, input(f"Please input the spaned vector: ").split()))
    vectors.append(vector_b)
    print(soln_vect_eqn(*vectors))
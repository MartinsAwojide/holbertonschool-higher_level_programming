def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new = []
        for num in matrix:
            new.append(list(map(lambda x: x*x, num)))
        return new

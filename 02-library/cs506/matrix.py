def get_determinant(matrix, sum_det=0):
   
    # Base Case 2x2 Matrix
    if len(matrix) == 2 and len(matrix[0]) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det
 
    # create sub matrix
    for focus_col in range(len(matrix)): 
        # copy input matrix
        sub_matrix = matrix.copy() 

        # remove 1st row
        sub_matrix = sub_matrix[1:]
 
        # remove focus column
        for i in range(len(sub_matrix)): 
            sub_matrix[i] = sub_matrix[i][0:focus_col] + sub_matrix[i][focus_col+1:] 
 
        # check sign
        sign = (-1)**(focus_col % 2)

        # recursion
        sub_det = get_determinant(sub_matrix)

        # sum up determinants of sub matrices
        sum_det += sign * matrix[0][focus_col] * sub_det
 
    return sum_det

print(get_determinant([[1,2,3],[4,5,6],[7,8,9]]))
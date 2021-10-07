from cs506 import matrix
import pytest
import numpy as np

def test_matrix_3x3_all_positive():
    test_mat = np.array([[1,2,3],[4,5,6],[7,8,10]])
    expected = np.linalg.det(test_mat)
    test_det = matrix.get_determinant(test_mat)

    test_mat.tolist()
    assert test_det == expected

def test_matrix_3x3_all_negative():
    test_mat = np.array([[-1,-2,-3],[-4,-5,-6],[-77,-88,-99]]) 
    expected = np.linalg.det(test_mat)

    test_mat.tolist()
    test_det = matrix.get_determinant(test_mat)

    assert test_det == expected

def test_matrix_5x5_negative_and_positive():
    test_mat = np.array([[-10,-9,-8,-7,-6],[-5,-4,-3,-2,-1],[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,999]])
    expected = np.linalg.det(test_mat)
    test_det = matrix.get_determinant(test_mat)

    test_mat.tolist()
    assert test_det == expected


#test_matrix_3x3_all_positive()
#test_matrix_3x3_all_negative()
#test_matrix_5x5_negative_and_positive()
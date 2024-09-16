from matrix_determinant import calculate_determinant
from matrix_adjugate import calculate_adjugate
import numpy as np

def calculate_inverse(matrix, results):
    determinant = calculate_determinant(matrix)
    if determinant == 0:
        raise ValueError("Matrix is singular, cannot calculate inverse.")

    adjugate_matrix = calculate_adjugate(matrix)
    
    inverse_matrix = np.array(adjugate_matrix) / determinant

    # Solve for x, y, z using the inverse matrix
    inverse_result = np.dot(inverse_matrix, results)

    # ปัดค่าผลลัพธ์ให้เป็นจำนวนเต็ม
    return np.round(inverse_result).astype(int)

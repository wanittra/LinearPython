import numpy as np

def calculate_adjugate(matrix):
    matrix = np.array(matrix)
    n = matrix.shape[0]
    
    # Create cofactor matrix
    cofactors = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            sub_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactors[i, j] = ((-1) ** (i + j)) * np.linalg.det(sub_matrix)

    # Transpose the cofactor matrix to get the adjugate matrix
    adjugate_matrix = cofactors.T

    # ปัดค่าทั้งหมดให้เป็นจำนวนเต็ม
    return np.round(adjugate_matrix).astype(int).tolist()

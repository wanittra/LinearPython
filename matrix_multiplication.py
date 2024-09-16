import numpy as np

def multiply_matrices(A, B):
    try:
        result = np.dot(A, B)
        return result
    except Exception as e:
        raise ValueError("Matrix multiplication failed: " + str(e))
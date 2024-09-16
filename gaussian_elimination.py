import numpy as np

def gaussian_elimination(matrix, results):
    augmented_matrix = np.array(matrix, dtype=float)
    results = np.array(results, dtype=float)

    n = len(results)
    for i in range(n):
        # Pivot
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        results[i], results[max_row] = results[max_row], results[i]

        for j in range(i+1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]
            results[j] -= factor * results[i]

    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (results[i] - np.dot(augmented_matrix[i, i+1:], x[i+1:])) / augmented_matrix[i, i]

    return x
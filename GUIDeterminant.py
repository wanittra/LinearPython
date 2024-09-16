import tkinter as tk
from tkinter import messagebox
from matrix_determinant import calculate_determinant


def create_matrix_entries(size, root):
    # Create a new window to input matrix values
    input_window = tk.Toplevel(root)
    input_window.title("Input Matrix Values")
    input_window.geometry("400x300")

    tk.Label(input_window, text="Enter the matrix values row by row:").pack(pady=10)

    entry_rows = []
    for i in range(size):
        tk.Label(input_window, text=f"Row {i+1}:").pack(pady=5)
        entry = tk.Entry(input_window, width=50)
        entry.pack(pady=5)
        entry_rows.append(entry)

    def on_submit():
        try:
            matrix = []
            for i in range(size):
                row_values = entry_rows[i].get().split()
                if len(row_values) != size:
                    raise ValueError(f"Row {i+1} should have exactly {size} values.")
                matrix.append([float(x) for x in row_values])

            determinant = calculate_determinant(matrix)

            result_window = tk.Toplevel(root)
            result_window.title("Determinant Result")
            result_window.geometry("300x200")

            result_text = tk.Text(result_window, wrap=tk.WORD)
            result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            result_text.insert(tk.END, f"Determinant = {determinant}\n")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    submit_button = tk.Button(input_window, text="Submit", command=on_submit)
    submit_button.pack(pady=20)

    input_window.wait_window()

def get_matrix_size_window(root):
    def on_size_submit():
        try:
            size = int(size_entry.get().strip())
            if size <= 0:
                raise ValueError("Matrix size must be a positive integer.")
            create_matrix_entries(size, root)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    size_window = tk.Toplevel(root)
    size_window.title("Matrix Size")
    size_window.geometry("300x200")

    tk.Label(size_window, text="Enter the size of the matrix (e.g., '3' for 3x3):").pack(pady=10)
    size_entry = tk.Entry(size_window, width=20)
    size_entry.pack(pady=5)

    size_submit_button = tk.Button(size_window, text="Submit", command=on_size_submit)
    size_submit_button.pack(pady=20)

    size_window.wait_window()

def run_determinant_gui():
    root = tk.Tk()
    root.title("Matrix Determinant")
    root.geometry("400x300")

    tk.Label(root, text="Matrix Determinant Calculator").pack(pady=20)

    start_button = tk.Button(root, text="Start", command=lambda: get_matrix_size_window(root))
    start_button.pack(pady=20)

    root.mainloop()
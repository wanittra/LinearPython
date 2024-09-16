import tkinter as tk
from tkinter import messagebox
import numpy as np
from matrix_multiplication import multiply_matrices


def get_matrix_input_window(root, matrix_name, rows, cols):
    def on_submit():
        nonlocal matrix
        try:
            matrix = []
            for i in range(rows):
                row_values = entry_rows[i].get().split()
                if len(row_values) != cols:
                    raise ValueError(f"Row {i+1} should have exactly {cols} values.")
                matrix.append([int(x) for x in row_values])
            input_window.destroy()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    matrix = []
    input_window = tk.Toplevel(root)
    input_window.title(f"Input for Matrix {matrix_name}")
    input_window.geometry("500x300")

    tk.Label(input_window, text=f"Enter values for Matrix {matrix_name} ({rows}x{cols}):").pack(pady=10)

    entry_rows = []
    for i in range(rows):
        tk.Label(input_window, text=f"Row {i+1}:").pack(pady=5)
        entry = tk.Entry(input_window, width=50)
        entry.pack(pady=5)
        entry_rows.append(entry)

    submit_button = tk.Button(input_window, text="Submit", command=on_submit)
    submit_button.pack(pady=20)

    input_window.wait_window()
    return matrix

def run_multiplication_gui():
    def on_calculate():
        try:
            rows_a = int(rows_entry_a.get())
            cols_a = int(cols_entry_a.get())
            rows_b = int(rows_entry_b.get())
            cols_b = int(cols_entry_b.get())

            if cols_a != rows_b:
                raise ValueError("Number of columns of Matrix A must equal the number of rows of Matrix B for multiplication.")

            A = get_matrix_input_window(root, "A", rows_a, cols_a)
            B = get_matrix_input_window(root, "B", rows_b, cols_b)

            result = multiply_matrices(A, B)

            result_window = tk.Toplevel(root)
            result_window.title("Multiplication Result")
            result_window.geometry("600x400")
            result_text = tk.Text(result_window, wrap=tk.WORD)
            result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            result_text.insert(tk.END, f"Matrix A ({rows_a}x{cols_a}):\n")
            for row in A:
                result_text.insert(tk.END, ' '.join(map(str, row)) + '\n')

            result_text.insert(tk.END, f"\nMatrix B ({rows_b}x{cols_b}):\n")
            for row in B:
                result_text.insert(tk.END, ' '.join(map(str, row)) + '\n')

            result_text.insert(tk.END, f"\nMatrix A*B ({rows_a}x{cols_b}):\n")
            for row in result:
                result_text.insert(tk.END, ' '.join(map(str, row)) + '\n')

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Matrix Multiplication")
    root.geometry("400x300")

    tk.Label(root, text="Matrix A - Rows:").pack(pady=5)
    rows_entry_a = tk.Entry(root)
    rows_entry_a.pack(pady=5)

    tk.Label(root, text="Matrix A - Columns:").pack(pady=5)
    cols_entry_a = tk.Entry(root)
    cols_entry_a.pack(pady=5)

    tk.Label(root, text="Matrix B - Rows:").pack(pady=5)
    rows_entry_b = tk.Entry(root)
    rows_entry_b.pack(pady=5)

    tk.Label(root, text="Matrix B - Columns:").pack(pady=5)
    cols_entry_b = tk.Entry(root)
    cols_entry_b.pack(pady=5)

    calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
    calculate_button.pack(pady=20)

    root.mainloop()
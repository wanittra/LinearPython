import tkinter as tk
from tkinter import messagebox
from matrix_inverse import calculate_inverse
from matrix_determinant import calculate_determinant
from matrix_adjugate import calculate_adjugate


def show_inverse_explanation():
    explanation_window = tk.Toplevel()
    explanation_window.title("Explanation: Matrix Inverse")
    explanation_window.geometry("400x300")

    explanation_text = (
    "Example of an equation \n"
    "[ 2 3 -4 ] [ x ] = [ 20 ] \n"
    "[ 1 1  2 ] [ y ] = [ 19 ] \n"
    "[ 2 1  1 ] [ z ] = [ 23 ] \n"
    "\n Input : \n"
    " Row 1 : 2 3 -4 20 \n" 
    " Row 2 : 1 1  2 19  \n"
    " Row 3 : 2 1  1 23 \n"
    " \n Determinant \n"
    " [ 2 3 -4 ]  \n"
    " [ 1 1  2 ]  \n"
    " [ 2 1  1 ] \n"
    " \n Adjugate Matrix: Cofactor -> Transpose \n"
    " \n A−1 = 1 / det(A)⋅adj(A) \n "
    )

    tk.Label(explanation_window, text=explanation_text, justify="left").pack(padx=20, pady=20)
    
    next_button = tk.Button(explanation_window, text="ถัดไป", command=lambda: open_input_window(explanation_window))
    next_button.pack(pady=10)

def open_input_window(parent_window):
    parent_window.destroy()  # ปิดหน้าต่างคำอธิบาย

    input_window = tk.Toplevel()
    input_window.title("Input for Inverse Calculation")
    input_window.geometry("400x300")

    tk.Label(input_window, text="Enter the augmented matrix (each row with 4 values):").pack(pady=10)

    entry_rows = []
    for i in range(3):
        tk.Label(input_window, text=f"Row {i+1}:").pack(pady=5)
        entry = tk.Entry(input_window, width=50)
        entry.pack(pady=5)
        entry_rows.append(entry)

    def on_submit():
        try:
            matrix = []
            results = []
            for i in range(3):
                row_values = entry_rows[i].get().split()
                if len(row_values) != 4:
                    raise ValueError(f"Row {i+1} should have exactly 4 values.")
                matrix.append([float(x) for x in row_values[:-1]])
                results.append(float(row_values[-1]))

            # คำนวณ determinant
            determinant = calculate_determinant(matrix)
            if determinant == 0:
                raise ValueError("Matrix is singular, cannot calculate inverse.")

            # คำนวณ adjugate
            adjugate_matrix = calculate_adjugate(matrix)

            # คำนวณ inverse
            inverse_result = calculate_inverse(matrix, results)

            # สร้างหน้าต่างใหม่สำหรับแสดงผล
            result_window = tk.Toplevel()
            result_window.title("Inverse Calculation Result")
            result_window.geometry("400x400")

            result_text = tk.Text(result_window, wrap=tk.WORD)
            result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            # แสดงผล determinant
            result_text.insert(tk.END, f"Determinant = {int(determinant)}\n\n")

            # แสดงผล adjugate matrix
            result_text.insert(tk.END, "Adjugate Matrix:\n")
            for row in adjugate_matrix:
                result_text.insert(tk.END, f"{row}\n")

            result_text.insert(tk.END, "\n")

            # แสดงผล inverse result
            result_text.insert(tk.END, f"Inverse Result:\n")
            result_text.insert(tk.END, f"x = {inverse_result[0]}\n")
            result_text.insert(tk.END, f"y = {inverse_result[1]}\n")
            result_text.insert(tk.END, f"z = {inverse_result[2]}\n")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    submit_button = tk.Button(input_window, text="Submit", command=on_submit)
    submit_button.pack(pady=20)

def run_inverse_gui():
    root = tk.Tk()
    root.title("Matrix Inverse")
    root.geometry("400x300")

    tk.Label(root, text="Matrix Inverse Solver").pack(pady=20)

    start_button = tk.Button(root, text="Start", command=show_inverse_explanation)
    start_button.pack(pady=20)

    root.mainloop()
    
# [ 2 3 -4 ] [ x ] = [ 20 ]
# [ 1 1  2 ] [ y ] = [ 19 ]
# [ 2 1  1 ] [ z ] = [ 23 ]
# Row 1 : 2 3 -4 20 
# Row 2 : 1 1  2 19 
# Row 3 : 2 1  1 23 
# Determinant 
# [ 2 3 -4 ] 
# [ 1 1  2 ] 
# [ 2 1  1 ] '
# Adjugate Matrix: Cofactor -> Transpose
# A−1 = 1 / det(A)⋅adj(A)
# ___________________________

# Determinant = 11

# Adjugate Matrix:
# [-1, -7, 10]
# [3, 10, -8]
# [10, -8, -1]

# Inverse Result:
# x = 7
# y = 6
# z = 3
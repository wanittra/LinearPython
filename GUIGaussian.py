import tkinter as tk
from tkinter import messagebox
from gaussian_elimination import gaussian_elimination


def show_instructions(root):
    def open_input_window():
        instructions_window.destroy()
        get_matrix_input_window(root)
    
    instructions_window = tk.Tk()
    instructions_window.title("Instructions for Gaussian Elimination")
    instructions_window.geometry("500x300")

    tk.Label(instructions_window, text="Instructions for Gaussian Elimination", font=("Helvetica", 16)).pack(pady=10)

    tk.Label(instructions_window, text="To solve a system of linear equations using Gaussian Elimination, follow these steps:", font=("Helvetica", 12)).pack(pady=5)
    
    instructions = (
        "1. Enter the augmented matrix for the system of equations.\n"
        "2. Each row should contain the coefficients of the variables followed by the constant term, separated by spaces.\n"
        "   Example: '2 3 -4 20' represents the equation 2x + 3y - 4z = 20.\n"
        "3. Ensure that you provide exactly 4 values for each row (3 coefficients and 1 constant).\n"
        "4. Click 'Submit' to calculate the solution for x, y, and z."
    )
    tk.Label(instructions_window, text=instructions, justify=tk.LEFT).pack(pady=10)

    tk.Button(instructions_window, text="Continue", command=open_input_window).pack(pady=20)

    instructions_window.mainloop()

def get_matrix_input_window(root):
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

            solution = gaussian_elimination(matrix, results)

            result_window = tk.Toplevel(root)
            result_window.title("Gaussian Elimination Result")
            result_window.geometry("300x200")

            result_text = tk.Text(result_window, wrap=tk.WORD)
            result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            result_text.insert(tk.END, "Result:\n")
            result_text.insert(tk.END, f"x = {solution[0]}\n")
            result_text.insert(tk.END, f"y = {solution[1]}\n")
            result_text.insert(tk.END, f"z = {solution[2]}\n")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    input_window = tk.Toplevel(root)
    input_window.title("Input for Gaussian Elimination")
    input_window.geometry("400x300")

    tk.Label(input_window, text="Enter the augmented matrix (each row with 4 values):").pack(pady=10)

    entry_rows = []
    for i in range(3):
        tk.Label(input_window, text=f"Row {i+1}:").pack(pady=5)
        entry = tk.Entry(input_window, width=50)
        entry.pack(pady=5)
        entry_rows.append(entry)

    submit_button = tk.Button(input_window, text="Submit", command=on_submit)
    submit_button.pack(pady=20)

    input_window.wait_window()

def run_gaussian_gui():
    root = tk.Tk()
    root.title("Gaussian Elimination")
    root.geometry("400x300")

    tk.Label(root, text="Gaussian Elimination Solver", font=("Helvetica", 16)).pack(pady=20)

    start_button = tk.Button(root, text="Start", command=lambda: show_instructions(root))
    start_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run_gaussian_gui()
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import GUIDeterminant
import GUIGaussian
import GUIInverse
import GUIMultiplication

def open_multiplication_gui():
    GUIMultiplication.run_multiplication_gui()

def open_gaussian_gui():
    GUIGaussian.run_gaussian_gui()

def open_determinant_gui():
    GUIDeterminant.run_determinant_gui()

def open_inverse_gui():
    GUIInverse.run_inverse_gui()

def main():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("300x400")  # Adjusted size to fit more buttons

    btn_multiplication = ttk.Button(root, text="Matrix Multiplication", command=open_multiplication_gui)
    btn_multiplication.pack(pady=10)

    btn_determinant = ttk.Button(root, text="Matrix Determinant", command=open_determinant_gui)
    btn_determinant.pack(pady=10)

    btn_inverse = ttk.Button(root, text="Matrix Inverse", command=open_inverse_gui)
    btn_inverse.pack(pady=10)
    
    btn_gaussian = ttk.Button(root, text="Gaussian Elimination", command=open_gaussian_gui)
    btn_gaussian.pack(pady=10)


    root.mainloop()

if __name__ == "__main__":
    main()
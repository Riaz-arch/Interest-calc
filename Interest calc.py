import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        simple_interest = (principal * rate * time) / 100

        compound_interest = principal * ((1 + (rate / 100)) ** time - 1)

        result_text = f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
        messagebox.showinfo("Interest Calculation", result_text)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Time Period (in years):").grid(row=1, column=0, padx=10, pady=10)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=10)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_button.grid(row=3, columnspan=2, pady=20)

root.mainloop()
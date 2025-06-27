
# Basic Calculator using Tkinter
# Created by: Student

import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_click(event):
    button_text = event.widget.cget("text")
    current_text = input_field.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Something went wrong!")
            input_field.delete(0, tk.END)
    elif button_text == "C":
        input_field.delete(0, tk.END)
    else:
        input_field.insert(tk.END, button_text)

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
input_field = tk.Entry(root, font=("Arial", 18), bd=8, relief=tk.SUNKEN, justify="right")
input_field.pack(fill=tk.X, padx=10, pady=10)

# Frame for buttons
btns_frame = tk.Frame(root)
btns_frame.pack()

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Creating and placing buttons
for row in buttons:
    row_frame = tk.Frame(btns_frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(row_frame, text=btn, font=("Arial", 16), relief=tk.RAISED, bd=3)
        button.pack(side="left", expand=True, fill="both", padx=1, pady=1)
        button.bind("<Button-1>", on_click)

# Run the app
root.mainloop()

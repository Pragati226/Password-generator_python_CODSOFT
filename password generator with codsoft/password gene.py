import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(password_length_entry.get())
        if length < 1:
            raise ValueError("Password length must be greater than 0")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(tk.END, password)
    except ValueError as e:
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(tk.END, "Invalid Length")

def reset_fields():
    user_name_entry.delete(0, tk.END)
    password_length_entry.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#FFA07A")  # Light Salmon background color

user_name_label = tk.Label(root, text="Enter User Name:", font=("Helvetica", 12), bg="#FFA07A")
user_name_label.grid(row=0, column=0, padx=10, pady=10)

password_length_label = tk.Label(root, text="Enter Password Length:", font=("Helvetica", 12), bg="#FFA07A")
password_length_label.grid(row=1, column=0, padx=10, pady=10)

generated_password_label = tk.Label(root, text="Generated Password:", font=("Helvetica", 12), bg="#FFA07A")
generated_password_label.grid(row=2, column=0, padx=10, pady=10)

user_name_entry = tk.Entry(root, font=("Helvetica", 12), width=20)
user_name_entry.grid(row=0, column=1, padx=10, pady=10)

password_length_entry = tk.Entry(root, font=("Helvetica", 12), width=20)
password_length_entry.grid(row=1, column=1, padx=10, pady=10)

generated_password_entry = tk.Entry(root, font=("Helvetica", 12), width=20)
generated_password_entry.grid(row=2, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#20B2AA", fg="white", command=generate_password)
generate_button.grid(row=3, column=1, padx=10, pady=10)

accept_button = tk.Button(root, text="Accept", font=("Helvetica", 12, "bold"), bg="#20B2AA", fg="white", command=root.quit)
accept_button.grid(row=4, column=0, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12, "bold"), bg="#20B2AA", fg="white", command=reset_fields)
reset_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()

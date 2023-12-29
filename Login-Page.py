#Github:https://github.com/shahriyar00131
import tkinter as tk
from tkinter import messagebox

def login_page():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login", "Login Was Successful")
    else:
        messagebox.showerror("Error", "Username Or Password  Is Not Correct")

root = tk.Tk()
root.title("Login Page")
root.geometry("400x250")

label_username = tk.Label(root, text="Username")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()


login_button = tk.Button(root, text="Login", command=login_page)
login_button.pack()

root.mainloop()

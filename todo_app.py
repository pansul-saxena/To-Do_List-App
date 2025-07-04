import tkinter as tk
from tkinter import messagebox, filedialog

# Functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task can't be empty!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Heading
label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
label.pack(pady=10)

# Listbox to display tasks
listbox = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12), selectbackground="skyblue")
listbox.pack(pady=10)

# Entry to type task
entry = tk.Entry(root, font=("Helvetica", 12), width=30)
entry.pack(pady=5)

# Button Frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

# Buttons
add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

save_btn = tk.Button(btn_frame, text="Save Tasks", width=12, command=save_tasks)
save_btn.grid(row=1, column=0, padx=5, pady=5)

load_btn = tk.Button(btn_frame, text="Load Tasks", width=12, command=load_tasks)
load_btn.grid(row=1, column=1, padx=5, pady=5)

# Load previous tasks if any
load_tasks()

# Run the app
root.mainloop()

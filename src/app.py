import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = "data/tasks.json"

def load_tasks():
    if not os.path.exists("data"):
        os.makedirs("data")
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Load existing tasks
tasks = load_tasks()

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

update_listbox()

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Remove Task", command=remove_task).pack(pady=5)

root.mainloop()

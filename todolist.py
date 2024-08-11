from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to update a selected task
def update_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get()
        if new_task:
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"[Completed] {task}")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Initialize the main window

root =tk.Tk()

root.title("To-Do List")
root.geometry("500x500+0+0")
root.resizable(width=False,height=False)

# Create and place the widgets
frame_tasks = tk.Frame(root)
frame_tasks.place(x=5,y=95)

listbox_tasks = tk.Listbox(frame_tasks, width=77, height=20, selectmode=tk.SINGLE)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=77)
entry_task.place(x=5,y=20)

button_add_task = tk.Button(root, text="Add Task", command=add_task,background="green")
button_add_task.place(x=20,y=50)

button_update_task = tk.Button(root, text="Update Task", command=update_task,background="yellow")
button_update_task.place(x=100,y=50)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task,bg="red")
button_delete_task.place(x=200,y=50)

button_complete_task = tk.Button(root, text="Complete Task", command=complete_task,bg="green")
button_complete_task.place(x=300,y=50)

# Start the GUI event loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "todofy_data.json"

class TodoFy:
    def __init__(self, root):
        self.root = root
        self.root.title("Todofy - To-Do List Application")
        self.root.geometry("450x500")
        self.root.config(bg="#282c34")

        self.tasks = []
        self.load_tasks()

        # Create the input frame for new tasks
        input_frame = tk.Frame(self.root, bg="#282c34")
        input_frame.pack(pady=20)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(input_frame, textvariable=self.task_var, font=("Segoe UI", 14), width=25)
        self.task_entry.grid(row=0, column=0, padx=(0,10))

        add_button = tk.Button(input_frame, text="Add Task", command=self.add_task, bg="#61afef", fg="white", 
                               font=("Segoe UI", 12), width=10, relief="flat")
        add_button.grid(row=0, column=1)

        # Create the list frame with scrollbar to display tasks
        list_frame = tk.Frame(self.root, bg="#282c34")
        list_frame.pack()

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_frame, width=45, height=15, font=("Segoe UI", 14), bd=0, fg="white", 
                                  bg="#3b4048", selectbackground="#61afef", activestyle="none", yscrollcommand=scrollbar.set)
        self.listbox.pack()

        scrollbar.config(command=self.listbox.yview)

        # Frame for buttons to complete, update, or delete tasks
        button_frame = tk.Frame(self.root, bg="#282c34")
        button_frame.pack(pady=20)

        complete_button = tk.Button(button_frame, text="Complete Task", command=self.complete_task, bg="#98c379", fg="white", 
                                    font=("Segoe UI", 12), width=14, relief="flat")
        complete_button.grid(row=0, column=0, padx=5)

        update_button = tk.Button(button_frame, text="Update Task", command=self.update_task, bg="#e5c07b", fg="white", 
                                  font=("Segoe UI", 12), width=14, relief="flat")
        update_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="#e06c75", fg="white", 
                                  font=("Segoe UI", 12), width=14, relief="flat")
        delete_button.grid(row=0, column=2, padx=5)

        self.refresh_listbox()

    def load_tasks(self):
        # Load tasks from the JSON file if it exists; otherwise initialize empty list
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    self.tasks = json.load(f)
            except Exception:
                self.tasks = []

    def save_tasks(self):
        # Save tasks to the JSON file
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def refresh_listbox(self):
        # Refresh the listbox to show current tasks, marking completed ones visually
        self.listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            display_text = task["task"]
            if task.get("completed"):
                display_text += " ✔"  # Add checkmark to completed tasks
            self.listbox.insert(tk.END, display_text)
            # Color completed tasks gray
            if task.get("completed"):
                self.listbox.itemconfig(index, fg="#7f848e")
            else:
                self.listbox.itemconfig(index, fg="white")

    def add_task(self):
        # Add a new task entered by the user
        task_text = self.task_var.get().strip()
        if not task_text:
            messagebox.showwarning("Empty Task", "Please enter a task.")
            return
        self.tasks.append({"task": task_text, "completed": False})
        self.task_var.set("")
        self.save_tasks()
        self.refresh_listbox()

    def complete_task(self):
        # Mark the selected task as completed
        try:
            index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("No selection", "Please select a task to complete.")
            return
        self.tasks[index]["completed"] = True
        self.save_tasks()
        self.refresh_listbox()

    def update_task(self):
        # Update the text of the selected task via a popup dialog
        try:
            index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("No selection", "Please select a task to update.")
            return
        current_task = self.tasks[index]["task"]
        new_task = simpledialog.askstring("Update Task", "Edit the selected task:", initialvalue=current_task)
        if new_task is None:
            return
        new_task = new_task.strip()
        if new_task == "":
            messagebox.showwarning("Invalid Task", "Task cannot be empty.")
            return
        self.tasks[index]["task"] = new_task
        self.save_tasks()
        self.refresh_listbox()

    def delete_task(self):
        # Delete the selected task after confirmation
        try:
            index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("No selection", "Please select a task to delete.")
            return
        confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete the selected task?")
        if confirm:
            del self.tasks[index]
            self.save_tasks()
            self.refresh_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoFy(root)
    root.mainloop()



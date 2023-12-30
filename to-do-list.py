import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with Alarms")

        self.tasks = []
        self.task_var = tk.StringVar()
        self.alarm_var = tk.StringVar()
        self.alarm_var.set("Select time")

        self.create_widgets()

    def create_widgets(self):
        # Task entry
        tk.Label(self.root, text="Task:").grid(row=0, column=0, padx=5, pady=5)
        entry_task = tk.Entry(self.root, textvariable=self.task_var)
        entry_task.grid(row=0, column=1, padx=5, pady=5)

        # Alarm time dropdown
        tk.Label(self.root, text="Alarm Time:").grid(row=1, column=0, padx=5, pady=5)
        alarm_options = ["Select time"] + [f"{i:02d}:00" for i in range(24)]
        alarm_dropdown = tk.OptionMenu(self.root, self.alarm_var, *alarm_options)
        alarm_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Add task button
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # To-Do List
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Remove task button
        remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_task(self):
        task = self.task_var.get()
        alarm_time = self.alarm_var.get()

        if task and alarm_time != "Select time":
            alarm_time = datetime.strptime(alarm_time, "%H:%M")
            task_data = {"task": task, "alarm_time": alarm_time}
            self.tasks.append(task_data)
            self.task_listbox.insert(tk.END, f"{task} - {alarm_time.strftime('%H:%M')}")
        else:
            messagebox.showwarning("Warning", "Please enter a task and select an alarm time.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_data = self.tasks.pop(selected_index[0])
            self.task_listbox.delete(selected_index)
            messagebox.showinfo("Task Removed", f"Task '{task_data['task']}' removed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

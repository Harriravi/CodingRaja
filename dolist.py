import json
import os
from datetime import datetime


class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name} - Priority: {self.priority}, Due Date: {self.due_date}, Status: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []  # Initialize the tasks attribute as an empty list
        self.load_tasks()


    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                data = json.load(file)
                for task_data in data:
                    task = Task(task_data['name'], task_data['priority'], task_data['due_date'])
                    task.completed = task_data['completed']
                    self.tasks.append(task)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            data = []
            for task in self.tasks:
                data.append({
                    'name': task.name,
                    'priority': task.priority,
                    'due_date': task.due_date,
                    'completed': task.completed
                })
            json.dump(data, file, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]
        self.save_tasks()

    def mark_task_as_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                self.save_tasks()

    def display_tasks(self):
        for task in self.tasks:
            print(task)


def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            if not due_date:
                due_date = None
            else:
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
                    continue

            task = Task(name, priority, due_date)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            name = input("Enter task name to remove: ")
            todo_list.remove_task(name)
            print("Task removed successfully!")

        elif choice == "3":
            name = input("Enter task name to mark as completed: ")
            todo_list.mark_task_as_completed(name)
            print("Task marked as completed!")

        elif choice == "4":
            print("\nTasks:")
            if todo_list.tasks:
                todo_list.display_tasks()
            else:
                print("No tasks to display.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

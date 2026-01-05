import json
import os

TASKS_FILE = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                tasks = json.load(file)
        except:
            tasks = []
    else:
        tasks = []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_id():
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task():
    description = input("Enter task description: ").strip()
    if description:
        tasks.append({"id": get_next_id(), "description": description, "completed": False})
        print("Task added successfully!")
    else:
        print("Description cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("\nTo-Do List:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"{task['id']}. {task['description']} [{status}]")

def mark_completed():
    view_tasks()
    try:
        task_id = int(input("\nEnter task ID to mark as completed: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print("Task marked as completed!")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Enter a number.")

def delete_task():
    view_tasks()
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        global tasks
        tasks = [task for task in tasks if task["id"] != task_id]
        print("Task deleted successfully!")
    except ValueError:
        print("Invalid input. Enter a number.")

def display_menu():
    print("\n=== To-Do List Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def main():
    load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
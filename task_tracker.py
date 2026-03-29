import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
        return []
    
def save_tasks(tasks):
    with open(TASK_FILE) as f:
        json.dump(tasks, f, indent=4)

def add_tasks(tittle, category="General"):
    tasks = load_tasks()
    tasks.append({"tittle": tittle, "category": category, "done": False})
    save_tasks(tasks)
    print(f"Task added : {tittle}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "X"
        print(f"{i}. {task['tittle']} [{task['category']}] - {status}")

def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index-1]["done"] = True
        save_tasks()
        print(f"Task completed : {tasks[index-1]['tittle']}")
    else:
        print("Invalid tasks number.")

def delete_tasks(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"Task deleted {removed['tittle']}")
    else:
        print("Invalid task number.")

# Example use

if __name__ == "__main__":
    print("Backend Developer Learning Tracker")
    print("commands: add, list, complete, delete, quit")

    while True:
        cmd = input("\nEnter command : ").strip().lower()
        if cmd == "add":
            tittle = input("Task tittle : ")
            category = input("Category (e.g., Python, Databases, APIs) : ")
            add_tasks(tittle, category)
        elif cmd == "list":
            list_tasks()
        elif cmd == "complete":
            index = int(input("Task number to complete : "))
            complete_task(index)
        elif cmd == "delete":
            index = int(input("Task number to delete"))
            delete_tasks(index)
        elif cmd == "quit":
            break
        else:
            print("Unknown command.")

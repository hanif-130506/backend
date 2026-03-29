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
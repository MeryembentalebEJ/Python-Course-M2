import json
import os
from task_manager.logger import setup_logger

TASKS_FILE = os.getenv("TASKS_FILE_PATH", "tasks.json")
logger = setup_logger()

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description, priority):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Added task: {task}")
    print("Task added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} (Priority: {task['priority']})")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(new_tasks):
        print("Task not found.")
        return
    save_tasks(new_tasks)
    logger.info(f"Deleted task with ID: {task_id}")
    print("Task deleted.")
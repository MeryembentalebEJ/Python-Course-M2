
import argparse
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")
    add_parser.add_argument("--priority", default="low", help="Priority (low, medium, high)")

    # List Tasks
    subparsers.add_parser("list", help="List all tasks")

    # Delete Task
    delete_parser = subparsers.add_parser("delete", help="Delete a task by ID")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description, args.priority)
    elif args.command == "list":
        list_tasks()
    elif args.command == "delete":
        delete_task(args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

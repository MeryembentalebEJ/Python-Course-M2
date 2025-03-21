import unittest
import os
import json
from task_manager.core import add_task, delete_task, load_tasks, save_tasks

TEST_FILE = "test_tasks.json"
os.environ["TASKS_FILE_PATH"] = TEST_FILE

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        save_tasks([])

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_add_task(self):
        add_task("Test task", "high")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task")
        self.assertEqual(tasks[0]["priority"], "high")

    def test_delete_task(self):
        add_task("Task to delete", "low")
        tasks = load_tasks()
        task_id = tasks[0]["id"]
        delete_task(task_id)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

if __name__ == "__main__":
    unittest.main()
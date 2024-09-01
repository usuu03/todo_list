import json
import os
from datetime import datetime


FILE_TASKS = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_TASKS):
        return []
    with open(FILE_TASKS, 'r') as file:
        return json.load(file)
        


# Function to save tasks to JSON file
def save_task(tasks):
    with open(FILE_TASKS, 'w') as file:
        json.dump(tasks, file, indent=3)
        
        
        
# Function to add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'TO DO',
        'createdAt': str(datetime.now(tz=None)),
        'updatedAt': str(datetime.now(tz=None))
    }
    tasks.append(task)
    save_task(tasks)
    print(f"Task has been successfully saved with ID: {task_id}")

# Function to update a task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = str(datetime.now())
            save_task(tasks)
            print(f"You have successfully updated the task with ID: {task_id}")
            return
        else:
            print(f"Task with ID: {task_id} not found, please try again")

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

# function update_task(id, new_description):
# load the tasks
# find the task with the given id
# if task is found:
# update the task's description and updatedAt
# save the updated list of tasks
# print success message with the task id
# else:
# print task not found message    
# def save_tasks():
    
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

# Function to delete a task

# function delete_task(id):
# load the tasks
# filter out the task with the given id from the list
# save the updated list of tasks
# print success message with the task id

def delete_task(taks_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != taks_id]
    save_task(tasks)
    print(f"Successfully deleted task with ID: {taks_id}")
# Function to mark a task as in progress

# function mark_in_progress(id):
# load the tasks
# find the task with the given id
# if task is found:
# update the task's status to 'in-progress' and updatedAt
# save the updated list of tasks
# print success message with the task id
# else:
# print task not found message

# Function to mark a task as done

# function mark_done(id):
# load the tasks
# find the task with the given id
# if task is found:
# update the task's status to 'done' and updatedAt
# save the updated list of tasks
# print success message with the task id
# else:
# print task not found message
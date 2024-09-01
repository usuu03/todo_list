# Import necessary modules
import json
import os
from datetime import datetime
import sys

# file path for storing tasks
FILE_TASKS = "tasks.json"

# Function to load tasks from JSON file
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
    task_id = max(task['id'] for task in tasks) + 1 if tasks else 1
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
def delete_task(taks_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != taks_id]
    save_task(tasks)
    print(f"Successfully deleted task with ID: {taks_id}")
    
    
# Function to update task status
def mark_task(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = str(datetime.now())
            save_task(tasks)
            print(f"You have successfully updated the status of the task with ID: {task_id}")
            return
        else:
            print(f"Task with ID: {task_id} not found, please try again")


# Function to list all tasks or filter by status
def list_tasks(status=None):
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == status or status is None:
            print(f"ID: {task['id']}, Description: {task['description']},Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

# Parse command line arguments
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [<args>]")
        return
    
    command = sys.argv[1]
    if command == "add":
        add_task(sys.argv[2])
    elif command == "update":
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete":
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress":
        mark_task(int(sys.argv[2]), 'IN PROGRESS')
    elif command == "mark-done":
        mark_task(int(sys.argv[2]), 'DONE')
    elif command == 'list':
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("")
      

if __name__ == "__main__":
    main()
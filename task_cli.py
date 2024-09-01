import json
import os
from datetime import datetime


FILE_TASKS = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_TASKS):
        return []
    with open(FILE_TASKS, 'r') as file:
        return json.load(file)
        
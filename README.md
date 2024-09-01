Here's a README template for your Task Tracker CLI project:

---

# **Task Tracker CLI**

Task Tracker CLI is a command-line application for managing your tasks. This simple tool allows you to add, update, delete, and list tasks, as well as track their status.

## **Features**

- **Add Tasks:** Create a new task with a description.
- **Update Tasks:** Modify the description of an existing task.
- **Delete Tasks:** Remove a task from the list.
- **Mark Tasks:** Update the status of a task (e.g., `todo`, `in-progress`, `done`).
- **List Tasks:** Display all tasks, or filter by status (e.g., show only tasks that are done).

## **Task Properties**

Each task includes the following properties:

- **id:** A unique identifier for the task.
- **description:** A short description of the task.
- **status:** The status of the task (`todo`, `in-progress`, `done`).
- **createdAt:** The date and time when the task was created.
- **updatedAt:** The date and time when the task was last updated.

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/task-tracker-cli.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd task-tracker-cli
   ```

3. **Ensure Python is installed on your system.**

4. **Run the CLI directly from the command line.**

## **Usage**

You can interact with the Task Tracker CLI by passing commands as arguments in the terminal.

### **Commands**

- **Add a new task:**

  ```bash
  python task_cli.py add "Buy groceries"
  ```

  Output: `Task added successfully (ID: 1)`

- **Update an existing task:**

  ```bash
  python task_cli.py update 1 "Buy groceries and cook dinner"
  ```

  Output: `Task updated successfully (ID: 1)`

- **Delete a task:**

  ```bash
  python task_cli.py delete 1
  ```

  Output: `Task deleted successfully (ID: 1)`

- **Mark a task as in progress:**

  ```bash
  python task_cli.py mark-in-progress 1
  ```

  Output: `Task marked as in-progress (ID: 1)`

- **Mark a task as done:**

  ```bash
  python task_cli.py mark-done 1
  ```

  Output: `Task marked as done (ID: 1)`

- **List all tasks:**

  ```bash
  python task_cli.py list
  ```

  Output: Displays all tasks.

- **List tasks by status:**

  ```bash
  python task_cli.py list done
  ```

  Output: Displays all tasks marked as `done`.

## **File Structure**

- `task_cli.py`: The main script for running the CLI application.
- `tasks.json`: The JSON file where tasks are stored.

## **Error Handling**

- The application gracefully handles scenarios where the user attempts to interact with a non-existent task or provide invalid input.

## **Contributing**

Feel free to fork this project, make changes, and submit a pull request. Contributions are always welcome!

## **License**

This project is licensed under the MIT License.

## **Contact**

If you have any questions, feel free to reach out:

- **Email:** usunobu.omijie@gmail.com

# Console-Based To-Do List Manager

**Simple Command-Line Task Manager** – A beginner-friendly Python console application for managing daily tasks with persistence.

**Student Information**  
- **Name**: Alabua Uche Christopher  
- **Department**: Cybersecurity  
- **Matriculation Number**: [24/13575]  

**Course**: (SEN201) Assignment  

## Project Overview

This is a console-based To-Do List application that allows users to:
- Add tasks
- View all tasks (with completion status)
- Mark tasks as completed
- Delete tasks
- Save tasks persistently to a JSON file
- Load tasks automatically on startup

The application uses only Python's standard library (no external packages required).

## Names and Nomenclatures (Design matches Implementation 100%)

The following names are used consistently throughout the system design documentation and the actual code:

- **Global list**: `tasks` → List of dictionaries, each task is:  
  `{"id": int, "description": str, "completed": bool}`

- **Data file**: `tasks.json` (persistent storage)

- **Key functions** (exact names used in code):
  - `load_tasks()`
  - `save_tasks()`
  - `get_next_id()`
  - `add_task()`
  - `view_tasks()`
  - `mark_completed()`
  - `delete_task()`
  - `display_menu()`
  - `main()`

- **Task dictionary keys**: `"id"`, `"description"`, `"completed"`

- **Menu options** (displayed and handled exactly as numbered):
  - 1 → Add Task
  - 2 → View Tasks
  - 3 → Mark Task as Completed
  - 4 → Delete Task
  - 5 → Exit

- **Status display**: `"Completed"` or `"Pending"`

## Features

- Menu-driven interface
- Auto-incrementing task IDs
- Mark tasks complete without deleting them
- Delete tasks by ID
- Persistent storage — tasks remain after program restart
- Basic input validation and error handling

## How to Run

1. Make sure you have Python 3 installed
2. Run the application:
   ```bash
   python todo_app.py

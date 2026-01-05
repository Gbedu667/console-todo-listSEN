# Console-Based To-Do List Application

This is a simple console-based To-Do List Manager implemented in Python. It demonstrates the full Software Development Life Cycle (SDLC) as part of an assignment.

## Project Overview

The application allows users to manage tasks via a command-line interface with the following features:
- Add new tasks
- View all tasks with status (Pending/Completed)
- Mark tasks as completed
- Delete tasks
- Persistent storage using a JSON file (`tasks.json`)

The project uses only Python's standard library (no external dependencies).

## SDLC Phases

### 1. Planning and Requirement Analysis
- **Objective**: Create a command-line To-Do List with persistence.
- **Functional Requirements**:
  - Menu-driven interface
  - Task operations: Add, View, Mark Completed, Delete
  - Auto-incrementing task IDs
  - Data saved to `tasks.json`
- **Non-Functional**: Simple, error-handling, console-only.

### 2. System Design
- **Data Structure**: List of dictionaries (`tasks`) where each task has `id`, `description`, `completed`.
- **Key Functions** (names match implementation):
  - `load_tasks()`
  - `save_tasks()`
  - `add_task()`
  - `view_tasks()`
  - `mark_completed()`
  - `delete_task()`
- **File**: `tasks.json` for persistence.

### 3. Implementation
- Single file: `todo_app.py`
- Main loop with menu handling.

### 4. Testing
- Manual testing of all features, edge cases (empty input, invalid IDs), and persistence.

### 5. Deployment
- Run with `python todo_app.py`

### 6. Maintenance
- Potential enhancements: Due dates, priorities, GUI.

## How to Run

1. Ensure Python 3 is installed.
2. Save the code as `todo_app.py`.
3. Run:
   ```bash
   python todo_app.py

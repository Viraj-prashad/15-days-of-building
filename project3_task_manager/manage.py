import json
import os


# ---------- Persistence ----------

def load_data():
    if not os.path.exists("tasks.json"):
        return {}, 1

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

        raw_tasks = data["tasks"]
        next_task_id = data["next_task_id"]

        tasks = {}
        for task_id, task_info in raw_tasks.items():
            tasks[int(task_id)] = task_info

        return tasks, next_task_id

    except (json.JSONDecodeError, KeyError):
        print("Error: tasks.json is empty or corrupted.")
        exit()


def save_data(tasks, task_id_counter):
    data = {
        "tasks": {},
        "next_task_id": task_id_counter
    }

    for task_id, task_info in tasks.items():
        data["tasks"][str(task_id)] = task_info

    try:
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")


# ---------- Command Handlers ----------

def handle_add(task_title, tasks, task_id_counter):
    if not task_title:
        print("Please provide a valid task title.")
        return task_id_counter

    tasks[task_id_counter] = {
        "title": task_title,
        "status": "pending"
    }

    print(f"Task '{task_title}' added with ID {task_id_counter}.")
    return task_id_counter + 1


def handle_view(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for task_id, task_info in tasks.items():
        print(f"{task_id}. {task_info['title']} [{task_info['status']}]")


def handle_done(task_id, tasks):
    if task_id not in tasks:
        print("Please provide a valid task ID.")
        return

    if tasks[task_id]["status"] == "completed":
        print("Task is already completed.")
        return

    tasks[task_id]["status"] = "completed"
    print(f"Task '{tasks[task_id]['title']}' marked as completed.")


def handle_delete(task_id, tasks):
    if task_id not in tasks:
        print("Please provide a valid task ID.")
        return

    deleted_task = tasks.pop(task_id)
    print(f"Task '{deleted_task['title']}' deleted.")


def handle_help():
    print("""
        Available commands:
        - greet                Show welcome message
        - add <task_title>     Add a new task
        - view                 View all tasks
        - done <task_id>       Mark a task as completed
        - delete <task_id>     Delete a task
        - exit                 Save tasks and exit
    """)


def greet():
    print("""
        Hello! Welcome to the Task Manager.

        Use 'help' to see available commands.
        Enjoy managing your tasks!
    """)


# ---------- Main Program ----------

def main():
    tasks, task_id_counter = load_data()

    while True:
        command = input("Enter command (type 'help' for options): ").strip()
        print() # For better readability

        if command == "exit":
            save_data(tasks, task_id_counter)
            print("Tasks saved. Goodbye!")
            break

        elif command == "greet":
            greet()
            print() # For better readability

        elif command == "help":
            handle_help()
            print() # For better readability

        elif command.startswith("add "):
            task_title = command[4:].strip()
            task_id_counter = handle_add(task_title, tasks, task_id_counter)
            print() # For better readability

        elif command == "view":
            handle_view(tasks)
            print() # For better readability

        elif command.startswith("done "):
            try:
                task_id = int(command[5:].strip())
            except ValueError:
                print("Please provide a valid task ID.")
                continue

            handle_done(task_id, tasks)
            print() # For better readability

        elif command.startswith("delete "):
            try:
                task_id = int(command[7:].strip())
            except ValueError:
                print("Please provide a valid task ID.")
                continue

            handle_delete(task_id, tasks)
            print() # For better readability

        else:
            print("Unknown command. Please enter a valid command.")
            print() # For better readability


if __name__ == "__main__":
    main()

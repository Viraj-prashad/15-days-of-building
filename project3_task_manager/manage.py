import json
import os


def load_data():
    if not os.path.exists("tasks.json"):
        return {}, 1


    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
        
        raw_tasks = data["tasks"]
        next_task_id = data["next_task_id"]

        # Convert task IDs back to integers
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

    # Convert task IDs to strings for JSON
    for task_id, task_info in tasks.items():
        data["tasks"][str(task_id)] = task_info

    try:
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")



def handle_add(task_title, tasks, task_id_counter):
    if not task_title:
        print("Please provide a valid task title.")
        return task_id_counter
    
    tasks[task_id_counter] = {"title": task_title, "status": "pending"}
    print(f"Task '{task_title}' with ID {task_id_counter} added to your task list.")
    return task_id_counter + 1



def handle_view(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for task_id, task_info in tasks.items():
        print(f"Task ID: {task_id}, Title: {task_info['title']}, Status: {task_info['status']}")



def handle_done(task_id, tasks):
    if task_id not in tasks:
        print("Please provide a valid task ID.")
        return

    tasks[task_id]["status"] = "completed"
    print(f"Task {tasks[task_id]['title']} with ID {task_id} marked as completed.")



def handle_delete(task_id, tasks):
    if task_id not in tasks:
            print("Please provide a valid task ID.")
            return

    deleted_task = tasks.pop(task_id)
    print(f"Task '{deleted_task['title']}' with ID {task_id} has been deleted.")
    


def handle_help():
    print('''
          Available commands:
          - greet: Display a welcome message and instructions.
          - add <task_title>: Add a new task with the specified title.
          - view: View all your tasks.
          - done <task_id>: Mark the task with the specified ID as completed.
          - delete <task_id>: Delete the task with the specified ID.
          - exit: Quit the program.
          ''')
    


def greet():
    print('''
          Hello! Welcome to the Task Manager.

          You can use help to see all available commands and how to use them.
          
          Enjoy managing your tasks!
          
          ''')
    


def handle_exit(tasks, task_id_counter):
    save_data(tasks, task_id_counter)
    print("Tasks saved. Goodbye!")
    exit()




tasks, task_id_counter = load_data()


while True:
    
    command = input("Enter a command (type 'exit' to quit or 'help' for commands): ")
    
    
    if command.lower() == "exit":
        handle_exit(tasks, task_id_counter)
    

    elif command == "greet":
        greet()
        

    elif command == "help":
        handle_help()
              
    
    elif command.startswith("add "):
        task_title = command[4:].strip()

        task_id_counter = handle_add(task_title, tasks, task_id_counter)


    elif command == "view":
        handle_view(tasks)

    
    elif command.startswith("done "):
        try:
            task_id = int(command[5:].strip())
        except ValueError:
            print("Please provide a valid task ID.")
            continue

        handle_done(task_id, tasks)


    elif command.startswith("delete "):
        try:
            task_id = int(command[7:].strip())
        except ValueError:
            print("Please provide a valid task ID.")
            continue

        handle_delete(task_id, tasks)


    else:
        print("Unknown command. Please try again.")

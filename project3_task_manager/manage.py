tasks = {}
task_id_counter = 1

while True:
    command = input("Enter a command (type 'exit' to quit): ")
    if command.lower() == "exit":
        break
    
    elif command == "greet":
        print('''
              Hello! Welcome to the Task Manager.

              You can use help to see all available commands and how to use them.
              
              Enjoy managing your tasks!
              
              ''')
        
    elif command == "help":
        print('''
              Available commands:
              - greet: Display a welcome message and instructions.
              - add <task_title>: Add a new task with the specified title.
              - view: View all your tasks.
              - done <task_id>: Mark the task with the specified ID as completed.
              - exit: Quit the program.
              ''')
    
    elif command.startswith("add "):
        task_title = command[4:].strip()
        if not task_title:
            print("Please provide a valid task title.")
            continue

        tasks[task_id_counter] = {"title": task_title, "status": "pending"}
        print(f"Task '{task_title}' with ID {task_id_counter} added to your task list.")
        task_id_counter += 1


    elif command == "view":
        if not tasks:
            print("No tasks available.")
            continue

        for task_id, task_info in tasks.items():
            print(f"Task ID: {task_id}, Title: {task_info['title']}, Status: {task_info['status']}")

    
    elif command.startswith("done "):
        task_id = int(command[5:].strip())
        if task_id not in tasks:
            print("Please provide a valid task ID.")
            continue

        tasks[task_id]["status"] = "completed"
        print(f"Task {tasks[task_id]['title']} with ID {task_id} marked as completed.")


    elif command.startswith("delete "):
        task_id = int(command[7:].strip())
        if task_id not in tasks:
            print("Please provide a valid task ID.")
            continue

        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' with ID {task_id} has been deleted.")


    else:
        print("Unknown command. Please try again.")

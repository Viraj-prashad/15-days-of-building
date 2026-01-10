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
              - status: View the status of your tasks.
              - done <task_id>: Mark the task with the specified ID as completed.
              - exit: Quit the program.
              ''')
    
    elif command.startswith("add "):
        task_title = command[4:]
        tasks[task_id_counter] = {"Title": task_title, "Status": "pending"}
        print(f"Task '{task_title}' added to your task list.")
        task_id_counter += 1

    elif command == "view":
        print("Here are your tasks:")
        for task_id, task_info in tasks.items():
            print(f"ID: {task_id}, Title: {task_info['Title']}, Status: {task_info['Status']}")

    elif command == "status":
        print("Here is the status of your tasks:")
        # This is where you would normally fetch and display task statuses from a database or list

    elif command.startswith("done "):
        task_id = command[5:]
        print(f"Task with ID '{task_id}' marked as completed. 'exit' to quit the program.")
        # This is where you would normally update the task status in a database or list

    else:
        print("Unknown command. Please try again.")

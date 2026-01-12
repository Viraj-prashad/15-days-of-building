from colorama import Fore, Style, init
import json
import os

# Initialize colorama
init(autoreset=True)


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
        print(f"{Fore.RED}❌ Error: tasks.json is empty or corrupted.{Style.RESET_ALL}")
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
        print(f"{Fore.RED}❌ Error saving data: {e}{Style.RESET_ALL}")


# ---------- Command Handlers ----------

def handle_add(task_title, tasks, task_id_counter):
    if not task_title:
        print(f"{Fore.YELLOW}⚠️  Please provide a valid task title.{Style.RESET_ALL}")
        return task_id_counter

    tasks[task_id_counter] = {
        "title": task_title,
        "status": "pending"
    }

    print(f"{Fore.GREEN}✅ Task '{Fore.CYAN}{task_title}{Fore.GREEN}' added with ID {Fore.MAGENTA}{task_id_counter}{Fore.GREEN}.{Style.RESET_ALL}")
    return task_id_counter + 1


def handle_view(tasks):
    if not tasks:
        print(f"{Fore.CYAN}ℹ️  No tasks available.{Style.RESET_ALL}")
        return

    print(f"{Fore.BLUE}{'═' * 50}{Style.RESET_ALL}")
    for task_id, task_info in tasks.items():
        status_color = Fore.GREEN if task_info['status'] == 'completed' else Fore.YELLOW
        status_icon = '✓' if task_info['status'] == 'completed' else '○'
        print(f"{Fore.MAGENTA}{task_id}.{Fore.RESET} {Fore.CYAN}{task_info['title']}{Fore.RESET} {status_color}[{status_icon} {task_info['status']}]{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{'═' * 50}{Style.RESET_ALL}")


def handle_done(task_id, tasks):
    if task_id not in tasks:
        print(f"{Fore.YELLOW}⚠️  Please provide a valid task ID.{Style.RESET_ALL}")
        return

    if tasks[task_id]["status"] == "completed":
        print(f"{Fore.CYAN}ℹ️  Task is already completed.{Style.RESET_ALL}")
        return

    tasks[task_id]["status"] = "completed"
    print(f"{Fore.GREEN}🎉 Task '{Fore.CYAN}{tasks[task_id]['title']}{Fore.GREEN}' marked as completed!{Style.RESET_ALL}")


def handle_delete(task_id, tasks):
    if task_id not in tasks:
        print(f"{Fore.YELLOW}⚠️  Please provide a valid task ID.{Style.RESET_ALL}")
        return

    deleted_task = tasks.pop(task_id)
    print(f"{Fore.RED}🗑️  Task '{Fore.CYAN}{deleted_task['title']}{Fore.RED}' deleted.{Style.RESET_ALL}")


def handle_help():
    print(f"""{Fore.YELLOW}{'═' * 60}
{Fore.CYAN}📋 Available commands:{Style.RESET_ALL}
{Fore.GREEN}  • add <task_title>{Fore.WHITE}     - Add a new task
{Fore.GREEN}  • view{Fore.WHITE}                 - View all tasks
{Fore.GREEN}  • done <task_id>{Fore.WHITE}       - Mark a task as completed
{Fore.GREEN}  • delete <task_id>{Fore.WHITE}     - Delete a task
{Fore.GREEN}  • exit{Fore.WHITE}                 - Save tasks and exit
{Fore.YELLOW}{'═' * 60}{Style.RESET_ALL}
    """)


def greet():
    print(f"""{Fore.MAGENTA}{'═' * 60}
{Fore.CYAN}✨ Hello! Welcome to the Task Manager ✨{Style.RESET_ALL}

{Fore.WHITE}  Use {Fore.GREEN}'help'{Fore.WHITE} to see available commands.
{Fore.WHITE}  Enjoy managing your tasks!
{Fore.MAGENTA}{'═' * 60}{Style.RESET_ALL}
    """)


# ---------- Main Program ----------

def manage():
    tasks, task_id_counter = load_data()
    greet()

    while True:
        command = input("Enter command (type 'help' for options): ").strip()
        print() # For better readability

        if command == "exit":
            save_data(tasks, task_id_counter)
            print(f"{Fore.GREEN}💾 Tasks saved. {Fore.MAGENTA}Goodbye! 👋{Style.RESET_ALL}")
            break

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
                print(f"{Fore.YELLOW}⚠️  Please provide a valid task ID.{Style.RESET_ALL}")
                continue

            handle_done(task_id, tasks)
            print() # For better readability

        elif command.startswith("delete "):
            try:
                task_id = int(command[7:].strip())
            except ValueError:
                print(f"{Fore.YELLOW}⚠️  Please provide a valid task ID.{Style.RESET_ALL}")
                continue

            handle_delete(task_id, tasks)
            print() # For better readability

        else:
            print(f"{Fore.RED}❌ Unknown command. Please enter a valid command. {Fore.CYAN}(type 'help' for options){Style.RESET_ALL}")
            print() # For better readability


if __name__ == "__main__":
    manage()
    print() # For better readability



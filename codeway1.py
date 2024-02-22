import os

def display_menu():
    print("\nTodo List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")

def view_tasks():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
        if tasks:
            print("\nTasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
        else:
            print("\nNo tasks yet!")

def add_task():
    task = input("\nEnter the task: ")
    with open('tasks.txt', 'a') as file:
        file.write(task + '\n')
    print("Task added successfully!")

def mark_task_done():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to mark as done: "))
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = "[Done] " + tasks[task_number - 1]
            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            print("Exiting the Todo List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    if not os.path.isfile('tasks.txt'):
        with open('tasks.txt', 'w'):
            pass  # Create an empty file if it doesn't exist
    main()

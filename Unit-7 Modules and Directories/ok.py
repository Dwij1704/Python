import os

def main():
    while True:
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def view_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")
    else:
        print("No tasks found.")

def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as f:
        f.write(f"{task}\n")
    print("Task added.")

def remove_task():
    view_tasks()
    task_index = int(input("Enter task number to remove: "))
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    with open("tasks.txt", "w") as f:
        for i, task in enumerate(tasks):
            if i != task_index - 1:
                f.write(task)
    print("Task removed.")

if __name__ == '__main__':
    main()

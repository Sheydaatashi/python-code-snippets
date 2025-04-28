tasks = []

def load_tasks():
    try:
        with open('todolist.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                task, priority = line.strip().split('|')
                tasks.append({'task': task, 'priority': priority})
    except FileNotFoundError:
        pass

def save_tasks():
    with open('todolist.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['priority']}\n")

def show_tasks():
    if not tasks:
        print("\nNo tasks in your list!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['task']} - Priority: {task['priority']}")

load_tasks()

while True:
    print("\n=== Todo List ===")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Change task")
    print("5. Exit")
    
    choice = input("\nWhat would you like to do? (1-5): ")
    
    if choice == '1':
        show_tasks()
        
    elif choice == '2':
        new_task = input("Enter new task: ")
        while True:
            task_priority = input('Enter task priority (high/medium/low): ').lower()
            if task_priority in ['high', 'medium', 'low']:
                break
            print("Please enter 'high', 'medium', or 'low'")
        tasks.append({'task': new_task, 'priority': task_priority})
        save_tasks()
        print("Task added!")
        
    elif choice == '3':
        show_tasks()
        if tasks:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted = tasks.pop(num - 1)
                    save_tasks()
                    print(f"Deleted: {deleted['task']}")
                else:
                    print("Invalid task number!")
            except:
                print("Please enter a valid number!")
                
    elif choice == '4':
        show_tasks()
        if tasks:
            try:
                num = int(input("Enter task number to change: "))
                if 1 <= num <= len(tasks):
                    new_task = input("Enter new task: ")
                    while True:
                        task_priority = input('Enter task priority (high/medium/low): ').lower()
                        if task_priority in ['high', 'medium', 'low']:
                            break
                        print("Please enter 'high', 'medium', or 'low'")
                    tasks[num - 1] = {'task': new_task, 'priority': task_priority}
                    save_tasks()
                    print("Task updated!")
                else:
                    print("Invalid task number!")
            except:
                print("Please enter a valid number!")
                
    elif choice == '5':
        save_tasks()
        print("Goodbye!")
        break
        
    else:
        print("Please choose a valid option (1-5)")
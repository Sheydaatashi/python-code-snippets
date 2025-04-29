from datetime import datetime

tasks = []

def load_tasks():
    try:
        with open('todolist.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                try:
                    task, priority, due_date = line.strip().split('|')
                    tasks.append({
                        'task': task,
                        'priority': priority,
                        'due_date': due_date
                    })
                except ValueError:
                    continue  
    except FileNotFoundError:
        pass

def save_tasks():
    with open('todolist.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['priority']}|{task['due_date']}\n")

def show_tasks():
    if not tasks:
        print("\nNo tasks in your list!")
        return
    
    try:
        sorted_tasks = sorted(tasks, key=lambda x: (datetime.strptime(x['due_date'], "%d/%m/%Y %H:%M"), priority_level(x['priority'])))
        print("\nYour Tasks:")
        for i, task in enumerate(sorted_tasks, 1):
            print(f"{i}. {task['task']}")
            print(f"   Due: {task['due_date']}")
            print(f"   Priority: {task['priority']}")
            print()
    except ValueError as e:
        print("\nError sorting tasks. Showing unsorted list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']}")
            print(f"   Due: {task['due_date']}")
            print(f"   Priority: {task['priority']}")
            print()

def priority_level(priority):
    levels = {'high': 1, 'medium': 2, 'low': 3}
    return levels.get(priority, 4)

def get_due_date():
    while True:
        date_str = input("Enter due date (dd HH:MM): ")
        try:
            parts = date_str.split()
            if len(parts) != 2:
                print("Please enter both day and time (example: 30 14:30)")
                continue
                
            day = int(parts[0])
            time = parts[1]
            
            today = datetime.now()
            
           
            if day < 1 or day > 31:
                print("Day must be between 1 and 31")
                continue
                
            
            if ':' not in time or len(time.split(':')) != 2:
                print("Time must be in HH:MM format (example: 14:30)")
                continue
            
            hours, minutes = map(int, time.split(':'))
            if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
                print("Invalid time. Hours: 0-23, Minutes: 0-59")
                continue
            
            due_date = datetime(today.year, today.month, day, hours, minutes)
            
            if due_date < today:
                if due_date.month == 12:
                    due_date = due_date.replace(year=due_date.year + 1, month=1)
                else:
                    due_date = due_date.replace(month=due_date.month + 1)
            
            return due_date.strftime("%d/%m/%Y %H:%M")
            
        except ValueError:
            print("Invalid format. Please use 'dd HH:MM' (example: 30 14:30)")

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
        due_date = get_due_date()
        tasks.append({
            'task': new_task,
            'priority': task_priority,
            'due_date': due_date
        })
        save_tasks()
        print("Task added!")
        
    elif choice == '3':
        show_tasks()
        if tasks:
            try:
                num = int(input("Enter task number to delete: "))
                sorted_tasks = sorted(tasks, key=lambda x: (datetime.strptime(x['due_date'], "%d/%m/%Y %H:%M"), priority_level(x['priority'])))
                if 1 <= num <= len(sorted_tasks):
                    task_to_delete = sorted_tasks[num - 1]
                    tasks.remove(task_to_delete)
                    save_tasks()
                    print(f"Deleted: {task_to_delete['task']}")
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
                    due_date = get_due_date()
                    tasks[num - 1] = {
                        'task': new_task,
                        'priority': task_priority,
                        'due_date': due_date
                    }
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
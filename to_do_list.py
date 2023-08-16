# initializes an empty list
tasks = []

# add task
def add_task(task):
    tasks.append(task)

# Remove task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task Not Found")

# show task
def show_task():
    if tasks:
        print("tasks")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No Tasks.")

# menu for a do_list
while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        task = input("Enter Task : ")
        add_task(task)
    elif choice == "2":
        task = input("Enter Task To Remove : ")
        remove_task(task)
    elif choice == "3":
        show_task()
    elif choice == "4":
        print("Exiting....")
        break
    else:
        print("Invalid Choice... Please Select Again")


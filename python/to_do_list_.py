tasks = []


def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


    def listTask():
        if not tasks:
            print("There are no tasks currently.")
        else:
            print("current Tasks:")
            for index, task in enumerate(tasks):
                print(f"#Tasks #{index}. {task}")


def deleteTask():
    try:
        taskToDelete = int(input("choose the # of the task you want to delee: "))
        if taskToDelete >= 0 and taskToDelete <len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} deleted from the list.")
        else:
            print(f"Task # {taskToDelete} is not in the list.")
    except:
        print("Invalid input")


if __name__ == "__main__":
    ### create a loop to run the app
    print("Welcome to the to do list app :")
    while True:
        print("\n")
        print("Please select one of the following options :")
        print("...........................................")
        print("1. Add anew task")
        print("2. delete a task")
        print("3. list a task")
        print("4. Quite")

        choice = input("Enter your choice :")
        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            break
        else:
            print("Invalid choice")

        print("Goodbye !!")
def display_menu():
    print("To-Do List Application")
    print("1.Add a task")
    print("2.View all tasks")
    print("3.Remove a task")
    print("4.Exit")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the application.Goodbye!")
            break
        else:
            print("Invalid choice. PLease try again")

if __name__ == "__main__":
    main()


        
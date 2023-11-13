from functions import show



todoList = []

while True:
    user_command = input("Type add,show,edit,complete,clear or exit: ")
    user_command = user_command.strip()
    match user_command:
        case 'add':

            task_toAdd = input("add a task: ") + '\n'

            with open('Todos.txt', 'r') as file:
                todoList = file.readlines()
            todoList.append(task_toAdd)
            with open('Todos.txt', 'w') as file:
                file.writelines(todoList)
        case 'show':
            show()
        case 'edit':
            todoList = show()
            indexToEdit = int(input("type the index number for task to edit: "))
            newTask = input("Please enter new task to replace it: ")
            todoList[indexToEdit - 1] = newTask
            with open('Todos.txt','w') as file:
                file.writelines(todoList)

        case 'complete':
            todoList = show()
            completedTaskIndex = int(input("type the index number for task to complete: "))
            todoList.pop(completedTaskIndex - 1)
            with open('Todos.txt','w') as file:
                file.writelines(todoList)
        case 'clear':
            todoList = show()
            toClear = input("Are you sure you want to clear all the tasks? enter Y in upper case :")
            if toClear == "Y":
                todoList =[]
                with open('Todos.txt', 'w') as file:
                    file.writelines(todoList)
                    print('All the tasks are cleared')

        case 'exit':
            break

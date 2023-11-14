from functions import show, getTodos

todoList = []

while True:
    user_command = input("Type add,show,edit,complete,clear or exit: ")
    user_command = user_command.strip()
    match user_command:
        case 'add':

            task_toAdd = input("add a task: ") + '\n'

            todoList = getTodos()
            todoList.append(task_toAdd)
            with open('Todos.txt', 'w') as file:
                file.writelines(todoList)
        case 'show':
            todoList = getTodos()
            show(todoList)
        case 'edit':
            show(todoList)
            todoList = getTodos()
            indexToEdit = int(input("type the index number for task to edit: "))
            newTask = input("Please enter new task to replace it: ")
            todoList[indexToEdit - 1] = newTask
            with open('Todos.txt','w') as file:
                file.writelines(todoList)

        case 'complete':
            show(todoList)
            todoList = getTodos()
            completedTaskIndex = int(input("type the index number for task to complete: "))
            todoList.pop(completedTaskIndex - 1)
            with open('Todos.txt','w') as file:
                file.writelines(todoList)
        case 'clear':
            show(todoList)
            todoList = getTodos()
            toClear = input("Are you sure you want to clear all the tasks? enter Y in upper case :")
            if toClear == "Y":
                todoList =[]
                with open('Todos.txt', 'w') as file:
                    file.writelines(todoList)
                    print('All the tasks are cleared')

        case 'exit':
            break

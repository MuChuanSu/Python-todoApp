def show():
    with open('Todos.txt', 'r') as file:
        todoList = file.readlines()

    for index, item in enumerate(todoList):
        print(f"{index + 1}.{item}")
    return todoList

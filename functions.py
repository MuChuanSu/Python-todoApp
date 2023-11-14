def show(ListToShow):
    getTodos()
    for index, item in enumerate(ListToShow):
        print(f"{index + 1}.{item}")

def getTodos():
    with open('Todos.txt', 'r') as file:
        todoList = file.readlines()
        return todoList
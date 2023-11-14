import streamlit as st
import functions


todos = functions.getTodos()
def add_todo():
    todo = st.session_state["new_todo"]
    '''This line gets the user input with the key "new_todo"' ''
    todos.append(todo+'\n')
    functions.writeTodos(todos)



st.title("My Todo App")
st.subheader("This is my Todo App")

for todo in todos:
    st.checkbox(todo)




st.text_input("Enter...", placeholder= "New task", on_change=add_todo, key="new_todo")

import streamlit as st
import functions


todos = functions.getTodos()


st.title("My Todo App")
st.subheader("This is my Todo App")

for todo in todos:
    st.checkbox(todo)




st.text_input("Enter...", placeholder= "New task")

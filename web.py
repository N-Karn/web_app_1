import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+ '\n')
    functions.write_todos(todos)


st.title("To-do App")
st.subheader("My first web app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]

st.text_input(label="", placeholder="Add a to-do...",
              on_change=add_todo, key='new_todo')





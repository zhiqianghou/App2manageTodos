import streamlit as st
import functions


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app increase your productivity")

for todo in todos:
	st.checkbox(todo)

st.text_input(label="", placeholder="Enter new todo:")




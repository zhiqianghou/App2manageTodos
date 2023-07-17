from venv.functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y:%H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index,item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index} - {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            todos = get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            # user_action = input("Type add, show, edit, complete or exit:")
            # user_action = user_action.strip()
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            todo_removed = todos[number].strip("\n")
            todos.pop(number)

            write_todos(todos)

            message = f"Todo item of {todo_removed} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Hey,you entered an unknown command")
print("Bye!")


from tasks import add_task, display_tasks

name = input("Enter your name: ")

print(f"Welcome, {name}!")

tasks = []

while True:
    task = input("Enter a task or type 'done' to finish: ")

    if task.lower() == "done":
        break

    add_task(tasks, task)

display_tasks(tasks)

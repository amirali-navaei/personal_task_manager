from tasks import add_task, display_tasks, save_tasks, load_tasks
name = input("enter your name: ")
print(f"welcome, {name}!")
tasks = load_tasks()


while True:
    task = input("enter a task or type done to finish: ")

    if task.lower() == "done":
        break

    add_task(tasks, task)
save_tasks(tasks)
display_tasks(tasks)

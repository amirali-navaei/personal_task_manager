import os
from dotenv import load_dotenv

from tasks import add_task, display_tasks, load_tasks, save_tasks


load_dotenv()


name = input("Enter your name: ")

print(f"Welcome, {name}!")


admin_choice = input("Do you want to enter Admin Mode? (yes/no): ")

if admin_choice.lower() == "yes":

    entered_password = input("Enter admin password: ")

    admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

    if entered_password == admin_password:
        print("Admin Mode activated.")
    else:
        print("Incorrect password.")


tasks = load_tasks()

while True:
    task = input("Enter a task or type 'done' to finish: ")

    if task.lower() == "done":
        break

    add_task(tasks, task)

save_tasks(tasks)

display_tasks(tasks)

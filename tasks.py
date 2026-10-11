def add_task(tasks, task , priority):
    tasks.append(task)


def display_tasks(tasks):
    print("\nYour tasks:")

    for task in tasks:
        print("-", task)
def save_tasks(tasks):
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()
def load_tasks():
    file = open("tasks.txt", "r")
    tasks = []
    for line in file:
        tasks.append(line.strip())
    file.close()
    return tasks
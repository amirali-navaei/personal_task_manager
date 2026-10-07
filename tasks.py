def add_task(tasks, task):
    tasks.append(task)


def display_tasks(tasks):
    print("\nYour tasks:")

    for task in tasks:
        print("-", task)
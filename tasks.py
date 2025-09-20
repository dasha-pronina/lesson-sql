from py_singleton import singleton

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from tasks_app.model import Base, Task


engine = create_engine("sqlite:///tasks_db.sqlite", echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


@singleton
class TasksStorage:
    def add(self, task_body):
        new_task = Task(body=task_body)
        session.add(new_task)
        session.commit()

    def remove(self, task_id):
        task_object = session.query(Task).get(
            task_id
        )  # начало запроса к бд по извлечению данных
        session.delete(task_object)
        session.commit()

    def change(self, task_id, new_task_body):
        task_object = session.query(Task).get(task_id)
        task_object.body = new_task_body

    def list(self):
        return session.query(Task).all()

    def change_status(self, task_id, new_status):
        task_object = session.query(Task).get(task_id)
        task_object.is_active = new_status
        session.commit()


# tasks = [] Задачи уже не tasks, а в TasksStorage

while True:
    command = (
        input("Введите команду [add, remove, change, list, exit, check, uncheck]: ")
        .strip()
        .lower()
    )

    if command == "add":
        element = input("Введите текст новой задачи: ")
        TasksStorage().add(element)
        print("Новая задача была добавлена успешно")

    elif command == "remove":
        number = int(input("Введите ID задания: "))

        try:
            TasksStorage().remove(number)
        except Exception:
            print("Не удалось удалить задание")
        else:
            print("Задание успешно удалено")

    elif command == "change":
        number = int(input("Введите ID задания: "))
        new_task = input("Введите новый текст задания: ")
        TasksStorage().change(number, new_task)
        print("Задание успешно изменено")

    elif command == "list":
        for task in TasksStorage().list():
            print(
                f"ID {task.id}, изменено {task.updated_at}, создано {task.created_at} - {task.is_active} - {task.body}"
            )

    elif command == "exit":
        break

    elif command == "check":
        number = int(input("Введите ID задания: "))
        TasksStorage().change_status(number, True)

    elif command == "uncheck":
        number = int(input("Введите ID задания: "))
        TasksStorage().change_status(number, False)

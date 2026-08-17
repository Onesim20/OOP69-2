import time
from functools import wraps


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


def is_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.role == "admin":
            return func(user, *args, **kwargs)
        else:
            print("У вас нет доступа")
    return wrapper


@is_admin
def delete_video(user):
    print("Видео удалено")


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time:.1f} секунд")
        return result
    return wrapper


@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")


admin = User("Ardager", "admin")
user = User("Bek", "user")

delete_video(admin)
delete_video(user)

download_video()
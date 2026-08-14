

def simple_decorator(func):
    def wrapper():
        print("до выполнения функции")
        func()
        print("после выполнения функции")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()

def greeting_decorator(func):
    def wrapper(name):
        print(f"Привет, {name}!")
        func(name)
        print(f"До свидания, {name}!")
    return wrapper

@greeting_decorator
def greet_person(name):
    print(f"Как дела, {name}!")

# greet_person("Онесим")

def repeat_decorator(value):
    def decorator(func):
        def wrapper(name):
            for i in range(value):
                func(name)
        return wrapper
    return decorator
@repeat_decorator(3)
def say_hello_Word(name):
    print(f"{name} say Hello Word !")

say_hello_Word("Онесим")

def class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            print("Это новый метод, добавленный декоратором.")

    return NewClass

class OldClass:
    def old_method(self):
        print("Это старый метод.")

test_obj = OldClass()

# import Lesson1 as ls

from lessons import Lesson1 as ls

onesim = ls.Hero("Онесим", 10, 100)
onesim.action()
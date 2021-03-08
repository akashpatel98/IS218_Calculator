def check(func):
    def wrapper():
        func()
    return wrapper



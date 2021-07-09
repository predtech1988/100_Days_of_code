def log_decorator(func):
    def wrapper(*args, **kwargs):
        a = func(*args)
        print(f" You called '{func.__name__}' it's returned -> {a} ")

    return wrapper


@log_decorator
def greet(name):
    return f"Hello {name}"


greet("Alex")

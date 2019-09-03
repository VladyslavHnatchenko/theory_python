"""Python Decorators."""


def trace(func):
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}() "
              f"with {args}, {kwargs}")

        original_result = func(*args, **kwargs)

        print(f"TRACE: {func.__name__}() "
              f"returned {original_result!r}")

        return original_result
    return wrapper


@trace
def say(name, line):
    return f"{name}: {line}"


def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# ------------------------------------------------------------------- #


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
# ------------------------------------------------------------------- #


def null_decorator(func):
    return func


# @uppercase
# def greet():
#     return "Hello!"


# greet = null_decorator(greet)


def greet():
    """Return a friendly greeting."""
    return "Hello!"


decorated_greet = uppercase(greet)

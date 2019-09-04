import functools
import time


def slow_down(func):
    """Sleep 1 second before calling the function."""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


countdown(3)

# ------------------------------------------------------------------- #
# def debug(func):
#     """Print the function signature and return value."""
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {value!r}")
#         return value
#     return wrapper_debug
#
#
# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} already, you are growing up!"
#
#
# make_greeting("Benjamin")
# make_greeting("Richard", age=112)
# make_greeting(name="Dorrisile", age=116)


# ------------------------------------------------------------------- #
# def timer(func):
#     """Print the runtime of the decorated function."""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__!r} in {run_time:4f} secs")
#         return value
#     return wrapper_timer
#
#
# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])
#
#
# waste_some_time(1)
# waste_some_time(559)
# waste_some_time(999)


# ------------------------------------------------------------------- #
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#
#     return wrapper_decorator


# ------------------------------------------------------------------- #
# def do_twice(func):
#     @functools.wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#
#     return wrapper_do_twice

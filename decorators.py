import functools
import time
import requests


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


def cache(func):
    """Keep a cache of previous function calls."""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num-1) + fibonacci(num-2)


print(fibonacci(10), "\n")
print(fibonacci(8), "\n")

# ------------------------------------------------------------------- #
# @count_calls
# def fibonacci(num):
#     if num < 2:
#         return num
#     return fibonacci(num-1) + fibonacci(num-2)
#
#
# print(fibonacci(10), "\n")
# print(fibonacci.num_calls)
# ------------------------------------------------------------------- #
#
# @count_calls
# def say_whee():
#     print("Whee!")
#
#
# say_whee()
# say_whee()
# print(say_whee.num_calls)
# ------------------------------------------------------------------- #
# def singleton(cls):
#     """Make a class a Singleton class(only one instance)."""
#     @functools.wraps(cls)
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         return wrapper_singleton.instance
#     wrapper_singleton.instance = None
#     return wrapper_singleton
#
#
# @singleton
# class TheOne:
#     pass
#
#
# first_one = TheOne()
# another_one = TheOne()
#
# print(id(first_one))
# print(id(another_one))
#
# print(first_one is another_one)
# print(first_one == another_one)

# ------------------------------------------------------------------- #
# class CountClass:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#         self.num_calls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f"call {self.num_calls} of {self.func.__name__!r}")
#         return self.func(*args, **kwargs)
#
#
# @CountClass
# def say_whee():
#     print("Whee!")
#
#
# say_whee()
# say_whee()
# print(say_whee.num_calls)

# ------------------------------------------------------------------- #
# class Counter:
#     def __init__(self, start=0):
#         self.count = start
#
#     def __call__(self):
#         self.count += 1
#         print(f"Current count is {self.count}")

# ------------------------------------------------------------------- #
# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print(f"[*] Execution time: {end-start} seconds.")
#         return return_value
#     return wrapper
#
#
# @benchmark
# def fetch_web_page(url):
#     web_page = requests.get(url)
#     return web_page.text
#
#
# web_page = fetch_web_page('https://google.com')
# print(web_page)

# ------------------------------------------------------------------- #
# def benchmark(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'[*] Execution time: {end-start} seconds.')
#     return wrapper
#
#
# @benchmark
# def fetch_web_page():
#     webpage = requests.get("https://google.com")
#
#
# fetch_web_page()

# ------------------------------------------------------------------- #
# def slow_down(func):
#     """Sleep 1 second before calling the function."""
#     @functools.wraps(func)
#     def wrapper_slow_down(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#     return wrapper_slow_down
#
#
# @slow_down
# def countdown(from_number):
#     if from_number < 1:
#         print("Liftoff!")
#     else:
#         print(from_number)
#         countdown(from_number - 1)
#
#
# countdown(3)

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

"""Python Generators."""
from itertools import islice

import requests
import re
import os


def simple_generator(val):
    while val > 0:
        val -= 1
        yield 1


gen_iter = simple_generator(5)
print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


f = fib()
print(list(islice(f, 0, 10)))

# ------------------------------------------------------------------- #
# def get_pages(link):
#     links_to_visit = []
#     links_to_visit.append(link)
#
#     while links_to_visit:
#         current_link = links_to_visit.pop(0)
#         page = requests.get(current_link)
#
#         for url in re.findall('<a href="([^"]+)">', str(page.content)):
#             if url[0] == '/':
#                 url = current_link + url[1:]
#             pattern = re.compile('https?')
#             if __name__ == '__main__':
#                 if pattern.match(url):
#                     links_to_visit.append(url)
#         yield current_link
#
#
# webpage = get_pages('https://www.bloomberg.com/markets/economics')
# for result in webpage:
#     print(result)

# ------------------------------------------------------------------- #

# def generate_filenames():
#     """Generate a sequence of opened files matching a specific extension."""
#
#     for dir_path, dir_names, file_names in os.walk("theory/"):
#         for file_name in file_names:
#             if file_name.endswith(".py"):
#                 yield open(os.path.join(dir_path, file_name))
#
#
# def cat_files(files):
#     """Takes in an iterable of filenames."""
#
#     for fname in files:
#         for line in fname:
#             yield line
#
#
# def grep_files(lines, pattern=None):
#     """Takes an iterable of lines."""
#
#     for line in lines:
#         if pattern in line:
#             yield line
#
#
# py_files = generate_filenames()
# py_file = cat_files(py_files)
# lines = grep_files(py_file, 'python')
# for line in lines:
#     print(line)

# ------------------------------------------------------------------- #
# def emit_lines(pattern=None):
#     lines = []
#     for dir_path, dir_names, file_names in os.walk('theory/'):
#         for file_name in file_names:
#             if file_name.endswith('.py'):
#                 for line in open(os.path.join(dir_path, file_name)):
#                     if pattern in line:
#                         lines.append(line)
#     return lines

# ------------------------------------------------------------------- #
# my_list = ["a", "b", "c", "d"]
# gen_obj = (x for x in my_list)
#
# for val in gen_obj:
#     print(val)
#
#
# def count_down(num):
#     print("Starting")
#     while num > 0:
#         yield num
#         num -= 1

# ------------------------------------------------------------------- #
# def bounded_repeater(value, max_repeats):
#     for i in range(max_repeats):
#         yield value

# ------------------------------------------------------------------- #
# class BoundedRepeater:
#     def __init__(self, value, max_repeats):
#         self.value = value
#         self.max_repeats = max_repeats
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count >= self.max_repeats:
#             raise StopIteration
#         self.count += 1
#         return self.value
#
#
# def bounded_repeater(value, max_repeats):
#     count = 0
#     while True:
#         if count >= max_repeats:
#             return
#         count += 1
#         yield value

# ------------------------------------------------------------------- #
# def repeat_three_times(value):
#     yield value
#     yield value
#     yield value

# ------------------------------------------------------------------- #
# class Repeater:
#     def __init__(self, value):
#         self.value = value
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.value
#
#
# def repeater(value):
#     while True:
#         yield value

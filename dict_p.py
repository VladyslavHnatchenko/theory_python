"""Dictionaries in Python."""

animals = {
    'cat': 1,
    'dog': 2,
    'bird': 3,
    'mouse': 4
}

print(animals)

for i in animals:
    print(i)

for d in animals:
    print(animals[d])

n = animals.items()
print(n)

for key, value in animals.items():
    print(key, 'is', value)

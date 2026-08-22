#6-1
my_friend = {
    "first_name": "ada",
    "last": "eze",
    "age": 20,
    "city": "enugu"
}

print(my_friend)


#6-1
favorite_numbers = {"steph": 7, "chidi": 3, "amara": 21, "tunde": 9, "ify": 12}

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")


#6-2
glossary = {
    "function": "a reusable block of code that performs a specific task",
    "dictionary": "a collection of key-value pairs",
    "list": "an ordered, changeable collection of items",
    "argument": "a value passed into a function when it's called",
    "loop": "a structure that repeats a block of code multiple times",
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:\n\t{meaning}")


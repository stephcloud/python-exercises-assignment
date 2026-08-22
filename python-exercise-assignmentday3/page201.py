#6-4
glossary = {
    "function": "a reusable block of code that performs a specific task",
    "dictionary": "a collection of key-value pairs",
    "list": "an ordered, changeable collection of items",
    "argument": "a value passed into a function when it's called",
    "loop": "a structure that repeats a block of code multiple times",
    "string": "a sequence of characters, used for text",
    "boolean": "a value that is either True or False",
    "index": "the position of an item in a list, starting at 0",
    "tuple": "an ordered, unchangeable collection of items",
    "module": "a file containing Python code you can import and reuse",
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:\n\t{meaning}")


#6-5
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}


for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")


print("\nRivers:")
for river in rivers.keys():
    print(river.title())


print("\nCountries:")
for country in rivers.values():
    print(country.title())

#6-5
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

people_to_poll = ["jen", "chukwuemeka", "sarah", "ngozi", "phil", "amaka"]

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll!")




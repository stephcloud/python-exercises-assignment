#6-7
person_1 = {"first_name": "John", "last_name": "Okafor", "age": 25, "city": "Enugu"}

person_2 = {"first_name": "Mary", "last_name": "Adeyemi", "age": 30, "city": "Lagos"}

person_3 = {"first_name": "David", "last_name": "Obi", "age": 22, "city": "Abuja"}

people = [person_1, person_2, person_3]

for person in people:
    print("\nPerson:")

    for key, value in person.items():
        print(f"{key}: {value}")

#6-8
pet_1 = {"animal": "dog", "owner": "John"}

pet_2 = {"animal": "cat", "owner": "Mary"}

pet_3 = {"animal": "parrot", "owner": "David"}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print("\nPet:")

    for key, value in pet.items():
        print(f"{key}: {value}")


#6-9
favorite_places = {
    "John": ["Enugu", "London", "Dubai"],
    "Mary": ["Lagos", "Paris"],
    "David": ["Abuja", "New York", "Cape Town"],
}

for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places:")

    for place in places:
        print(f"- {place}")


#6-10
favorite_numbers = {"John": [7, 10, 21], "Mary": [3, 8, 15], "David": [5, 12, 30]}

for person, numbers in favorite_numbers.items():
    print(f"\n{person}'s favorite numbers:")

    for number in numbers:
        print(number)


#6-11
cities = {
    "Enugu": {
        "country": "Nigeria",
        "population": 722664,
        "fact": "Enugu is known as the Coal City.",
    },
    "London": {
        "country": "United Kingdom",
        "population": 9000000,
        "fact": "London is home to Big Ben.",
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is home to the Eiffel Tower.",
    },
}

for city, information in cities.items():
    print(f"\nCity: {city}")

    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")

#6-12
cities = {
    "Enugu": {
        "country": "Nigeria",
        "population": 722664,
        "fact": "Enugu is known as the Coal City.",
        "language": "English",
        "currency": "Naira",
        "famous_food": "Abacha",
    },
    "London": {
        "country": "United Kingdom",
        "population": 9000000,
        "fact": "London is home to Big Ben.",
        "language": "English",
        "currency": "Pound Sterling",
        "famous_food": "Fish and chips",
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is home to the Eiffel Tower.",
        "language": "French",
        "currency": "Euro",
        "famous_food": "Croissant",
    },
}

for city, information in cities.items():
    print("\n======================")
    print(f"CITY: {city}")
    print("======================")

    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
    print(f"Language: {information['language']}")
    print(f"Currency: {information['currency']}")
    print(f"Famous food: {information['famous_food']}")


#6-12
cities = {
    "Enugu": {
        "country": "Nigeria",
        "population": 722664,
        "fact": "Enugu is known as the Coal City.",
        "language": "English",
        "currency": "Naira",
        "famous_food": "Abacha",
    },
    "London": {
        "country": "United Kingdom",
        "population": 9000000,
        "fact": "London is home to Big Ben.",
        "language": "English",
        "currency": "Pound Sterling",
        "famous_food": "Fish and chips",
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is home to the Eiffel Tower.",
        "language": "French",
        "currency": "Euro",
        "famous_food": "Croissant",
    },
}

for city, information in cities.items():
    print("\n======================")
    print(f"CITY: {city}")
    print("======================")

    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
    print(f"Language: {information['language']}")
    print(f"Currency: {information['currency']}")
    print(f"Famous food: {information['famous_food']}")
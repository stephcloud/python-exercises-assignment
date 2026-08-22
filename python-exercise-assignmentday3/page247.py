#8-3
def make_shirt(size,text):
    print(f"My T-shirt size is {size} and I want {text} to be printed on it, thank you. ")
make_shirt("xl", "El-roi")
make_shirt(text="El-roi", size="xl")

#8-4
def make_shirt(size="large", text="I love python"):
    print(f"My T-shirt size is {size} and I want {text} to be printed on it, thank you. ")


make_shirt()
make_shirt("medium")
make_shirt("small", "Hackathonafrica3.0")

#8-5
def describe_city(city, country="Nigeria"):
    print(f"{city} is in {country}")

describe_city("Lagos")
describe_city("Abuja")
describe_city("Tokyo","Japan")

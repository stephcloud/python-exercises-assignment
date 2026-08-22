#8-12
def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich("cheese")
make_sandwich("cheese", "lettuce", "tomato")
make_sandwich("turkey", "mustard", "onions", "pickles")

#8-13

def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


my_profile = build_profile(
    "steph", "neche", location="Enugu", field="software development", hobby="writing"
)

print(my_profile)

#8-14
def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)


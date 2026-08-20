#7-8
sandwich_orders = ['tuna', 'turkey', 'club', 'blt', 'egg salad']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)

#7-9
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'blt', 'pastrami', 'club']

print("Sorry, we're out of pastrami today.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

#7-10
active = True

while active:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    print(f"{name} would love to visit {place}.")

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        active = False
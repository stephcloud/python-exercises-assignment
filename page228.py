#7-4
topping = ''

while topping != 'quit':
    topping = input("Enter a pizza topping ('quit' to stop): ")
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")


#7-5
age = ''

while age != 'quit':
    age = input("Enter your age (or 'quit' to exit): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

#7-6
#Version 1
topping = ''

while topping != 'quit':
    topping = input("Enter a pizza topping ('quit' to stop): ")
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")


#Version 2
active = True

while active:
    topping = input("Enter a pizza topping ('quit' to stop): ")
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")


#Version 3
while True:
    topping = input("Enter a pizza topping ('quit' to stop): ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")


#7-7
while True:
    print("This loop never ends!")
    
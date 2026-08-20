# 4-10
fruits = ["mango", "apple", "pineapple", "kiwi", "grape", "orange", "banana"]
print("The first three items in the list are:")
print(fruits [:3])
print("\nThree items from the middle of the list are:")
print(fruits[2:5])
print("\nThe last three items in the list are:")
print(fruits[-3:])

#4-11
my_pizzas = ["margherita", "pepperoni", "hawaiian", "bbq chicken", "veggie"]
my_friend_pizzas= (my_pizzas[:])
print(my_friend_pizzas)

my_pizzas.append("four cheese")
my_friend_pizzas.append("spicy diavola")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in my_friend_pizzas:
    print(pizza)


# 4-12
my_pizzas = ["margherita", "pepperoni", "hawaiian", "bbq chicken", "veggie"]
my_friend_pizzas = my_pizzas[:]

my_pizzas.append("four cheese")
my_friend_pizzas.append("diavola")

print("My favorite pizza are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizza are:")
for pizza in my_friend_pizzas:
    print(pizza)

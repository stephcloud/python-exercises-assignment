#10-6
first_number = input("Enter a number: ")
second_number = input("Enter another number: ")

try:
    total = int(first_number) + int(second_number)
except ValueError:
    print("Sorry, please enter numbers only.")
else:
    print(f"The sum is {total}")

#10-7
print("Enter 'q' to quit at any time.\n")

while True:
    first_number = input("Enter a number: ")
    if first_number == "q":
        break

    second_number = input("Enter another number: ")
    if second_number == "q":
        break

    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, please enter numbers only.\n")
    else:
        print(f"The sum is {total}\n")

#10-8
try:
    with open("cats.txt") as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry, the file cats.txt could not be found.")
else:
    print(contents)

try:
    with open("dogs.txt") as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry, the file dogs.txt could not be found.")
else:
    print(contents)

#10-9
try:
    with open("cats.txt") as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)

try:
    with open("dogs.txt") as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)


#10-10
filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} could not be found.")
else:
    word_count = contents.lower().count("the")
    print(f"The word 'the' appears approximately {word_count} times.")

    word_count_with_space = contents.lower().count("the ")
    print(f"'the ' (with trailing space) appears {word_count_with_space} times.")
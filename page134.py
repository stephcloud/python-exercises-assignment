#4-3
for value in range(1, 21):
   print(value)

#4-4
for value in range(1, 1000001):
  print(value)

#4-5
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6
odd_numbers = list(range(1, 21, 2))

for numbers in odd_numbers:
    print(numbers)

#4-7
multiples = list(range(3, 31, 3))
for number in multiples:
    print(number)

#4-8
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
    print(cubes)

#4-9

cubes = []
cubes = [value**3 for value in range(1, 11)]
print(cubes)

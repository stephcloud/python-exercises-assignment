nums = input("Enter three numbers: ").split()
a, b, c = int(nums[0]), int(nums[1]), int(nums[2])

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is {largest}.")
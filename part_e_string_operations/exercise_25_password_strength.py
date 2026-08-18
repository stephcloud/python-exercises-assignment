password = "Pass@123"

has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)
long_enough = len(password) >= 8

if has_number and has_special and long_enough:
    print("Password is strong.")
else:
    print("Password is weak.")
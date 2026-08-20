#3-4
dinner_invite = ["lilian", "austine", "charles"]
print(dinner_invite)

print(f"Hey {dinner_invite[0]} I'm inviting to a dinner tonight ")
print(f"Hey {dinner_invite[1]} I'm inviting you to a dinner tonight ")
print(f"Hey {dinner_invite[2]} I'm inviting you to a dinner tonight ")

#3-5
dinner_invite = ["lilian", "austine", "charles"]
print(dinner_invite)

print(f"{dinner_invite[1]} won't make it to the dinner for some reasons ")

dinner_invite[1] = "kosi"
print(f"Hey {dinner_invite[0]} I'm inviting to a dinner tonight ")
print(f"hey {dinner_invite[1]} I'm inviting you to a dinner tonight ")
print(f"hey {dinner_invite[2]} I'm inviting you to a dinner tonight ")


#3-6
dinner_invite = ["lilian", "kosi", "charles"]
print(dinner_invite)

dinner_invite.insert(0, "chris")
dinner_invite.insert(1, "ada")
dinner_invite.insert(2, "kelly")
print(dinner_invite)

dinner_invite.insert(3, "James")
print(dinner_invite)

dinner_invite = ['chris', 'ada', 'kelly', 'James', 'lilian', 'kosi', 'charles']
print(dinner_invite)

dinner_invite.append("steph")
print(dinner_invite)

print(f"Hello, {dinner_invite[0]} you're invited to a dinner at De Castle tonight ")
print(f"Hello, {dinner_invite[1]} you're invited to a dinner at De Castle tonight ")
print(f"Hello, {dinner_invite[2]} you're invited to a dinner at De Castle tonight ")
print(f"Hello, {dinner_invite[3]} you're invited to a dinner at De Castle tonight ")
print(f"Hello, {dinner_invite[4]} you're invited to a dinner at De Castle tonight ")
print(f"Hello, {dinner_invite[5]} you're invited to a dinner at De Castle tonight ")
print(f"Hello, {dinner_invite[7]} you're invited to a dinner at De Castle tonight ")


#3-7
dinner_invite = ['chris', 'ada', 'kelly', 'James', 'lilian', 'kosi', 'charles', 'steph']

print("The new table won't arrive in time, so I can only invite two people for dinner.")

popped_guest = dinner_invite.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = dinner_invite.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = dinner_invite.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = dinner_invite.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = dinner_invite.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = dinner_invite.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

print(dinner_invite)

print(f"{dinner_invite[0]}, you're still invited to dinner!")
print(f"{dinner_invite[1]}, you're still invited to dinner!")


del dinner_invite[1]
print(dinner_invite)

del dinner_invite[0]
print(dinner_invite)

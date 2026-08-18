words = ["Python", "is", "amazing"]
sentence = ", ".join(words)
back_to_list = sentence.split(", ")

print(f"List to String: {sentence}")
print(f"String to List: {back_to_list}")
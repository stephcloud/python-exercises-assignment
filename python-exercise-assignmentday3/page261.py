#8-9
def show_messages(messages):
    for message in messages:
        print(message)


text_messages = ["hey, you free later?", "don't forget the meeting", "happy birthday!"]
show_messages(text_messages)


#8-10

def show_messages(messages):
    for message in messages:
        print(message)


text_messages = ["hey, you free later?", "don't forget the meeting", "happy birthday!"]

#8-11
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


text_messages = ["hey, you free later?", "don't forget the meeting", "happy birthday!"]
sent_messages = []

send_messages(text_messages, sent_messages)

print("\nOriginal list:", text_messages)
print("Sent list:", sent_messages)
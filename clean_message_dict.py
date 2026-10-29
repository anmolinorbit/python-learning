message = {"model": "gpt-3.5-turbo", "role": " ", "content": "Please write a Python function that counts the number of words in a given string." }
print(message)
keys_to_delete = []
for key , value in message.items():
    if value == " ":
        keys_to_delete.append(key)

for key in keys_to_delete:
    del message[key]

print(message)
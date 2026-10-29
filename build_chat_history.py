chat_history = []
chat_history.append({"role": "system", "content": "You are a helpful assistant."})
chat_history.append({"role": "user", "content": "Please write a Python function that counts the number of words in a given string."})
chat_history.append({"role": "assistant", "content": "Sure! Here is a Python function that counts the number of words in a given string:"})

print(chat_history)
print()

last_message = chat_history[-1]
print(last_message)
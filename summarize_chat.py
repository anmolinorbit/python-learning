chat_history = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Please write a Python function that counts the number of words in a given string."}, {"role": "system", "content": "Sure! Here is a Python function that counts the number of words in a given string:"}]

total_messages = len(chat_history)
user_count = 0
assistant_count = 0
for message in chat_history:
    if message["role"] == "user":
        user_count += 1
    elif message["role"] == "system":
        assistant_count += 1

last_message_object = chat_history[-1]
last_role = last_message_object["role"]
last_content = last_message_object["content"]

print(total_messages)
print(user_count)
print(assistant_count)
print(last_role)
print(last_content)


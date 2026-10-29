chat_history =  [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Please write a Python function that counts the number of words in a given string."}, {"role": "assistant", "content": "Sure! Here is a Python function that counts the number of words in a given string:"}]

longest_message = None
max_length = 0
for message in chat_history:
    content_length = len(message["content"])
    if content_length > max_length:
        max_length = content_length
        longest_message = message
if longest_message:
    print(longest_message["role"])
    print(max_length)
    print(longest_message["content"])
else:
    print("no chat history")

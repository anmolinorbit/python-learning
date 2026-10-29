message = {"role": "user", "content": "Please write a Python function that counts the number of words in a given string."}

context_message = message["content"]

word_list = context_message.split()
word_count = len(word_list)


print(message["role"])
print(context_message)
print(word_count)
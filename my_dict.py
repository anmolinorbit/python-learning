message = {"role": "assistant", "content": "Hello! How can I assist you today?"}
print(message["role"])
print(message["content"])
print(message.get("roles" , "No role found"))
message["language"] = "English"
message["content"] = "Hi there! How can I help you?"

for key , value in message.items():
    print(key , ":", value)
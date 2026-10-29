message = {"role": "assistant", "content": "Hello! How can I assist you today?"}
if "role" in message:
    print("Role exists in the dictionary.")
else:
    print("Role does not exist in the dictionary.")
if "content" in message:
    print("Content exists in the dictionary.")
else:
    print("Content does not exist in the dictionary.")
if "model" in message:
    print("Model exists in the dictionary.")
else:
    print("Model does not exist in the dictionary.")    
message = {"role": "assistant", "content": "Hello! How can I assist you today?"}
model_used = message.get("model", "No model found")
print(model_used)
print(message.get("role"))
print(message.get("content"))
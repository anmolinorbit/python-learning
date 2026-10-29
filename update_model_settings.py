message = {"model": "gpt-3.5-turbo", "temperature": 0.7, "max_tokens": 150}
print(message)

user_input = input("Enter new temperature 0.0 to 1.0: ")

try:
    new_temperature = float(user_input)
    message["temperature"] = new_temperature
    print(message)
except ValueError:
    print("Invalid input. Please enter a valid number.")
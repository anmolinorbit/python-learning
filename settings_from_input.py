model_input = input("Enter the model name: ")
temp_input = input("Enter the temperature value: ")
tokens_input = input("Enter the max tokens value: ")

try:
    temp_val = float(temp_input)
    tokens_val = int(tokens_input)
    settings = {
        "model": model_input,
        "temperature": temp_val,
        "max_tokens": tokens_val
    }
    print(settings)
except ValueError:
    print("Invalid input. Please enter valid numbers for temperature and max tokens.")
model_settings = {"model": "gpt-3.5-turbo", "temperature": 0.7, "max_tokens": 150}
print(model_settings.keys())
print(model_settings.values())
for key, value in model_settings.items():
    print(key, ":", value)
base_settings = {"model": "gpt-3.5-turbo", "temperature": 0.7, "max_tokens": 150}
user_settings = {"temperature": 0.9, "max_tokens": 200}
print(base_settings)
print(user_settings)

base_settings.update(user_settings)
print(base_settings)
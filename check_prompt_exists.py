prompts = ["what is the capital of France?", "what is the largest ocean on Earth?", "what is the tallest mountain in the world?", "what is the longest river in the world?"]
keywords = input("Enter keywords to search for in the prompts: ")
found = False
for prompt in prompts:
    if keywords in prompt:
        print(prompt)
        found = True
if not found:
    print("No prompts found containing the specified keywords.")
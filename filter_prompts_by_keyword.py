prompts = ["what is the capital of France?", "what is the largest ocean on Earth?", "what is the tallest mountain in the world?", "what is the longest river in the world?", "what is the largest desert in the world?", "what is the smallest country in the world?"]

keywords = input("Enter keywords to search for in the prompts: ")
match_count = 0
for prompt in prompts:
    if keywords in prompt:
        print(prompt)
        match_count += 1
if match_count == 0:
    print("No prompts found containing the specified keywords.")
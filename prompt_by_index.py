prompts = ["what is the capital of France?", "what is the largest ocean on Earth?", "what is the tallest mountain in the world?", "what is the longest river in the world?", "what is the largest desert in the world?"]
index = int(input("Enter an index (0-4): "))
if 0 <= index < len(prompts):
    print(prompts[index])
else:
    print("Invalid index. Please enter a number between 0 and 4.")
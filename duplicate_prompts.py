prompts = ["what is the capital of France?", "what is the largest ocean on Earth?", "what is the tallest mountain in the world?", "what is the longest river in the world?", "what is the largest desert in the world?", "what is the smallest country in the world?", "what is the most populous country in the world?", "what is the fastest land animal?", "what is the largest mammal in the world?", "what is the deepest part of the ocean?""what is the capital of France?", "what is the largest ocean on Earth?", "what is the tallest mountain in the world?", "what is the longest river in the world?", "what is the largest desert in the world?", "what is the smallest country in the world?", "what is the most populous country in the world?", "what is the fastest land animal?", "what is the largest mammal in the world?", "what is the deepest part of the ocean?"]
cleaned_prompts = []
for prompt in prompts:
    if prompt not in cleaned_prompts:
        cleaned_prompts.append(prompt)
print(len(prompts))
print(len(cleaned_prompts))
print(cleaned_prompts)


prompts = ["what is the capital of France?", "what is the largest ocean on Earth?", "what is the tallest mountain in the world?", "what is the longest river in the world?", "what is the largest desert in the world?", "what is the smallest country in the world?", "what is the most populous country in the world?", "what is the fastest land animal?", "what is the largest mammal in the world?", "what is the deepest part of the ocean?"]
longest_prompt =""
max_length = 0
for prompt in prompts:
    current_length = len(prompt)
    if current_length > max_length:
        max_length = current_length
        longest_prompt = prompt
print(longest_prompt)
print(max_length)
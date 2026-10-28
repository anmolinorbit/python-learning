prompts = ["what is the capital of France?", "what is the largest ocean on Earth?", "what is the tallest mountain in the world?", "what is the longest river in the world?", "what is the largest desert in the world?", "what is the smallest country in the world?", "what is the most populous country in the world?", "what is the fastest land animal?", "what is the largest mammal in the world?", "what is the deepest part of the ocean?"]

batch_size = 3
batch_number = 1
for i in range(0 , len(prompts) , batch_size):
    current_batch = prompts[i:i + batch_size]



    for prompt in current_batch:
        print(prompt)
    print()
    batch_number+=1
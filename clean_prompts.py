prompts = ["","explain    photosyntesis", " write a short poem" , "  how to build website"] 
cleaned_prompts = []
for prompt in prompts:
    cleaned_prompt = prompt.strip()
    if cleaned_prompt:
        cleaned_prompts.append(cleaned_prompt)
print(cleaned_prompts)
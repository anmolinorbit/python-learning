prompts = ["Explain black holes", "Explain the theory of relativity", "Explain the concept of time dilation", "Explain the concept of quantum entanglement", "Explain the concept of dark matter", "Explain the concept of dark energy", "Explain the concept of string theory", "Explain the concept of multiverse", "Explain the concept of wormholes", "Explain the concept of cosmic inflation"]
print(prompts[0])
print(prompts[-1])
print(len(prompts))

prompts.append("Explain the concept of gravitational waves")
print(prompts)
for prompt in prompts:
    print(prompt)
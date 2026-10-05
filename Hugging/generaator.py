from transformers import pipeline
chat= pipeline(
    "text-generation",
    model="openai-community/gpt2"
)

result = chat(
    "who is virat kohli",
    max_length=20
)

print(result)


from transformers import pipeline

pipe = pipeline("text-generation", model="distilbert/distilgpt2")
result=pipe("who is virat kohli")
print(result)
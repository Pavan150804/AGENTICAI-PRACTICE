from transformers import AutoTokenizer,AutoModelForCausalLM
import torch
tokenizer = AutoTokenizer.from_pretrained('openai-community/gpt2')
model = AutoModelForCausalLM.from_pretrained('openai-community/gpt2')
text = "Hi how are you..."
encoded_input = tokenizer(text, return_tensors='pt')
output = model.generate(**encoded_input,max_length=15)
output_text=tokenizer.decode(output[0],skip_special_tokens=True)
print(output_text)
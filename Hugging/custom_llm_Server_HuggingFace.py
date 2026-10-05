import os
from transformers import AutoModelForCausalLM, AutoTokenizer
# from huggingface_hub import login
# from openai import OpenAI
#import google as genai
# from google import genai
from fastapi import FastAPI
from pydantic import BaseModel
import torch


# os.environ["HF_TOKEN"] = ""
# #login("")

model_name = "gpt2"  # or any other variant
tokenizer = AutoTokenizer.from_pretrained(model_name,cache_dir="./models",token=os.getenv("HF_TOKEN"))
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./models",token=os.getenv("HF_TOKEN"))


#import torch

app = FastAPI()

class RequestData(BaseModel):
    prompt: str
    max_length: int = 20

@app.post("/generate")
async def generate_text(data: RequestData):
    inputs = tokenizer(data.prompt, return_tensors="pt")#.to("cuda")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=data.max_length)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(result)
    return {"generated_text": result}

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/geminiask")
# async def generate_ans(data: RequestData):
   
#     client = genai.Client(api_key="")

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=data.prompt
#     )
#     return response.text

    # use above code for google gemini and below code to use openai SDK for gemini model

    # client = OpenAI(
    #     api_key="",
    #     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    # )
    # print(data.prompt)
    # response = client.chat.completions.create(
    #     model="gemini-2.5-flash",
    #     messages=[
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {"role": "user",   "content": data.prompt}
    #     ]
    # )
    # return {"generated_text": response.choices[0].message.content}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

#{
# "prompt": "you question"
#}
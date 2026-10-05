from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from google.genai import types

app=FastAPI()

class RequestData(BaseModel):
    prompt:str
    
@app.post("/askgemini")
def generate(data:RequestData):
    client = genai.Client(api_key="")

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=data.prompt
    )
    return{"generated_text":response.text}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)
    
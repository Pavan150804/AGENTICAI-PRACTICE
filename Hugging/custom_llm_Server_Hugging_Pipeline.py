from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

generator = pipeline(
    "text-generation",
    model=r"D:\PythonPractice\models\models--gpt2\snapshots\607a30d783dfa663caf39e06633721c8d4cfcd7e"
)

class RequestData(BaseModel):
    prompt: str
    max_new_tokens: int = 30

@app.post("/generate")
async def generate_text(data: RequestData):

    result = generator(
        data.prompt,
        max_new_tokens=data.max_new_tokens
    )

    return {
        "generated_text": result[0]["generated_text"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
from google import genai
from google.genai import types

client = genai.Client(api_key="")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=["Explain how AI works in 50 words"],
    config=types.GenerateContentConfig(
        temperature=0.1,
        top_k=3,
        top_p=0.7,
        # max_output_tokens=200
        )
        
)
print(response.text)
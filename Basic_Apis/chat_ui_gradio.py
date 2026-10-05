import gradio as gr
from google import genai
from google.genai import types

client = genai.Client(api_key="")

def chat_fn(msg, history):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction="You are a helpful assitant.Please provide responses in clear and concise text in 50 words"),
        contents=msg
    )
    return response.text

gr.ChatInterface(
    fn=chat_fn,
    title="My Custom ChatGPT",
    description="Need help..."
).launch(
    server_name="0.0.0.0",
    server_port=7860,
    share=True
)
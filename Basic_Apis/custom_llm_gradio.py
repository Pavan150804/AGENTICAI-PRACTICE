import requests
import gradio as gr

API_URL = "http://localhost:8000/askgemini"

def chat_fn(message, history):
    try:
        # prmp = f"you are a helpful assistant. {message}"
        prmp=message

        resp = requests.post(
            API_URL,
            json={"prompt": prmp}
        )

        if resp.status_code == 200:
            return resp.json()["generated_text"]

        return f"Error {resp.status_code}: {resp.text}"

    except Exception as e:
        return f"API Error: {str(e)}"


gr.ChatInterface(
    fn=chat_fn,
    title="Locally deployed Chatbot"
).launch(
    server_name="0.0.0.0",
    server_port=7861,
    share=True
)
import gradio as gr

def chat(message,history):
    return f"Hello {message}"

demo = gr.ChatInterface(
    fn=chat,
)

demo.launch(server_name="0.0.0.0",server_port=8080,share=True)
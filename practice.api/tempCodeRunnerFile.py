import gradio as gr

def greet(message,history):
    return f"Hello {message}"

demo = gr.ChatInterface(
    fn=greet,
    inputs="text",
    outputs="text"
)

demo.launch()
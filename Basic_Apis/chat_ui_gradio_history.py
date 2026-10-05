import gradio as gr
from google import genai
from google.genai import types

client = genai.Client(api_key="")

def chat_fn(message, history):  #chat_fn(message="Hello", history=[])
   
    contents=[]
    
    
    # Keep only last 3 conversation turns 
    # MAX_TURNS = 3
    # history = history[-(MAX_TURNS * 2):]slicing from 6 index give me all elements
    
    MAX_MESSAGES = 6

    if len(history) > MAX_MESSAGES:
        history.pop(0)
        
    # while len(history)>MAX_MESSAGES:
    #     history.pop(0)
    
    
    
    #convert gradio history into gemini format
#     Gradio's chat history format typically uses:
# {
#     "role": "user",
#     "content": "Hello"
# }
# {
#     "role": "assistant",
#     "content": "Hi!"
# }
# So Gradio roles are:
# user
# assistant
# Gemini's API format uses:
# types.Content(
#     role="user",
#     ...
# )
# types.Content(
#     role="model",
#     ...
# )
# So Gemini roles are:
# user
# model

    for msg in history:
        if msg["role"]=="assistant":
           role="model"
        else:
            role="user"
        
        text=msg["content"]
        
        # Handle cases where content is stored as a list

        if isinstance(text, list):
            text=text[0]["text"]
        
        # {
        #     'role':'user',
        #     'content':[
        #         {
        #             'text':'hi',
        #             'type':'text'
        #         }
        #     ]
        # }
        
        contents.append(
            types.Content(
                role=role,
                parts=[types.Part.from_text(text=text)]
            )
        )

# Why do we need types.Content()?
# Gemini does not understand:
# ["Hello", "Hi there!", "What is Python?"]
# because it doesn't know:
# Who said "Hello"?
# Who said "Hi there!"?
# So we wrap each message in a Content object:
# types.Content(
#     role="user",
#     parts=[...]
# )
# which means:
# User: Hello

    contents.append(
        types.Content(
              role="user",
              parts=[types.Part.from_text(text=message)]
            )
        )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction="You are a helpful assistant.Please provide responses in clear and concise text in 50 words"),
        contents=contents
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
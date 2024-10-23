# chatbot_demo.py

# import dotenv
import os
import openai
from openai import OpenAI
# from openai import Completion


import gradio as gr
# from config import OPENAI_API_KEY
# from openai import OpenAI


client = OpenAI()


# Set the API key from the configuration file
openai.api_key = os.getenv("OPENAI_API_KEY")



def chat_V1(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant, I'd like to talk to a {input_text}."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content.strip()

def chatbot_response(input_text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"I'd like to talk to a {input_text}.",
        max_tokens=50  # You can adjust this for longer responses
    )
    return response.choices[0].text


# Create the Gradio interface
iface = gr.Interface(
    # fn=chatbot_response,
    fn=chat_V1,
    inputs=gr.Textbox(
        "text", label="Enter the type of bot you want to talk to (e.g., 'coding assistant' or 'therapist')"),
    outputs="text",
    live=True,
    # live=False
    title="Custom Chatbot",
    description="Select the type of bot you'd like to talk to and start the conversation."
)

iface.launch(share=True)
# iface.launch()
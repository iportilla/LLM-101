'''
 This file contains the functions for the chatbot.
 It demonstrates the use of the OpenAI API to generate responses to user input.
 v1.0 last update 10.22.24
'''
import openai
import dotenv
import os
import openai
from openai import OpenAI
from openai import Completion


#load dotenv
dotenv.load_dotenv()
#set openai api key
# openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create( 
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=1024
    )
    return response.choices[0].message.content.strip()


# Send a message to the chatbot
context = [{'role': 'user', 'content': 'How are you'}]        
response = get_completion_from_messages(messages=context)
print(response)

# context =[ {
#       "role": "user",
#       "content": [{ "type": "text", "text": "knock knock." }]
#     },
#     {
#       "role": "assistant",
#       "content": [{ "type": "text", "text": "Who's there?" }]
#     },
#     {
#       "role": "user",
#       "content": [{ "type": "text", "text": "Orange." }]
#     }
#   ]

# response = get_completion_from_messages(messages=context)
# print(response)
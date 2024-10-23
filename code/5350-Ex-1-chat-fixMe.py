import openai
import dotenv
import os
from openai import OpenAI
from openai import Completion


#load dotenv
dotenv.load_dotenv()
#set openai api key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Initialize the API client
client = OpenAI()


# Create a new completion session
completion = Completion(client=client)

# Send a message to the chatbot
response = completion.create(prompt="Hello, how are you?", max_tokens=1024)
print(response.choices[0].text)

#FixMe








# https://platform.openai.com/docs/overview

# from openai import OpenAI
# client = OpenAI()
# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "user", "content": "write a haiku about ai"}
#     ]
# )

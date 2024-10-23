"""
    This is a simple Flask app that uses OpenAI's GPT-3 API to generate responses to user input.
    It uses the OpenAI API to generate responses to user input.
    It was trained with pizza restaurant prompting.
    v1.0 last update 10.22.24

"""
import os
import openai
from openai import OpenAI
from flask import Flask, request, render_template
from dotenv import load_dotenv

# Load the OpenAI API key from the .env file
load_dotenv()
# openai.api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Initialize Flask app
app = Flask(__name__)

# Initialize conversation context
context = [{'role': 'system', 'content': """
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
[Your system prompt here]
"""}]

  # accumulate messages





# https://github.com/openai/openai-python



# Function to call OpenAI API using the new interface
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    # response = openai.ChatCompletion.create(
    response = client.chat.completions.create( 
        model=model,
        messages=messages,
        temperature=temperature,
    )
    # return response.choices[0].message['content'].strip()
    return response.choices[0].message.content.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    user_message = ""
    bot_response = ""

    if request.method == "POST":
        # Get the user input from the form
        user_message = request.form["user_input"]

        # Add user input to context
        context.append({"role": "user", "content": user_message})

        # Get bot response from OpenAI
        bot_response = get_completion_from_messages(context)

        # Add bot response to context
        context.append({"role": "assistant", "content": bot_response})

    return render_template("index.html", user_message=user_message, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
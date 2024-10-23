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
# context = [{'role': 'system', 'content': """
# You are OrderBot, an automated service to collect orders for a pizza restaurant. \
# [Your system prompt here]
# """}]

context = [{'role': 'system', 'content': """
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""}]  # accumulate messages



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
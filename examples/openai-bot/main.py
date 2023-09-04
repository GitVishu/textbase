from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """Welcome to the Psychology Chatbot!

You are now chatting with a virtual psychologist. Whether you have questions about mental health, want to explore psychological concepts, or simply need someone to talk to, I'm here to assist you.

Feel free to discuss topics like anxiety, depression, stress management, relationship issues, personal development, and any other psychological or emotional concerns you may have.

Please remember that I am an AI chatbot and not a substitute for professional psychological counseling or therapy. If you are experiencing a crisis or need immediate help, please reach out to a mental health professional or a crisis hotline.

To start, you can ask questions, share your thoughts, or describe any psychological issues you'd like to discuss, and I'll do my best to provide information, support, or guidance.
"""


@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }
# chatbot/chatbot.py

import re
import datetime

RESPONSES = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I help you with?"],
    "business_hours": "Our business hours are from 9 AM to 5 PM, Monday through Friday.",
    "goodbye": ["Goodbye! Have a great day!", "See you later!"],
    "thanks": ["You're welcome!", "Glad to help!"]
}

def get_response(user_input):
    user_input = user_input.lower()  # Lowercase input for easier matching

    if re.search(r"\b(hello|hi|hey)\b", user_input):
        return RESPONSES["greeting"][0]
    elif re.search(r"\b(hours|time|open|close|business)\b", user_input):
        return RESPONSES["business_hours"]
    elif re.search(r"\b(thanks|thank you|appreciate)\b", user_input):
        return RESPONSES["thanks"][0]
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return RESPONSES["goodbye"][0]
    else:
        return "I'm not sure about that. Could you ask something else?"

def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

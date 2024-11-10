import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

def preprocess_input(user_input):
    tokens = word_tokenize(user_input.lower())
    return tokens

def get_response(user_input):
    tokens = preprocess_input(user_input)
    if "hello" in tokens:
        return "Hi there! How can I help you today?"
    elif "thanks" in tokens:
        return "You're welcome!"
    elif "bye" in tokens:
        return "Goodbye!"
    else:
        return "I'm here to help with any questions you have."

def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

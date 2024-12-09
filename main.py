from utils import load_model, get_response

import tkinter as tk
from tkinter import scrolledtext
import json
import random
import pickle
import os

# Load the model from pickle
def load_model(model_path='models/chatbot_model.pkl'):
    try:
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")
        
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        exit(1)

# Get response from intents.json file
def get_response(tag, intents_file="intents.json"):
    try:
        if not os.path.exists(intents_file):
            raise FileNotFoundError(f"Intents file not found at: {intents_file}")
        
        with open(intents_file, 'r') as file:
            intents = json.load(file)
        
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
        return "I don't understand that."
    except Exception as e:
        print(f"Error getting response: {e}")
        return "Sorry, I encountered an error."

# Create a function to handle user input
def handle_user_input(event=None):
    user_input = user_input_field.get()
    if user_input.lower() == 'quit':
        root.quit()
    else:
        # Get a response based on the user input
        tag = 'greeting'  # In reality, this should be from your model's prediction
        response = get_response(tag)

        # Insert the user input and chatbot response into the chat window
        chat_window.insert(tk.END, f"You: {user_input}\n")
        chat_window.insert(tk.END, f"Chatbot: {response}\n")
        chat_window.yview(tk.END)  # Scroll to the bottom

        # Clear the input field after sending
        user_input_field.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create a scrollable chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_window.grid(row=0, column=0, columnspan=2)

# Create an input field for the user to type their message
user_input_field = tk.Entry(root, font=("Arial", 12), width=40)
user_input_field.grid(row=1, column=0)

# Create a button to send the message
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=handle_user_input)
send_button.grid(row=1, column=1)

# Bind the Enter key to send the message
root.bind('<Return>', handle_user_input)

# Run the application
root.mainloop()

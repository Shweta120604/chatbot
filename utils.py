import json
import random
import pickle
import os

# Modify the model loading function
def load_model(model_path='models/chatbot_model.pkl'):
    """
    Loads the chatbot model from the specified path using pickle.
    Args:
        model_path (str): The path to the saved model file (default: 'models/chatbot_model.pkl').
    Returns:
        model: The loaded model object.
    """
    try:
        # Check if the model file exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")
        
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        exit(1)

# Modify the get_response function
def get_response(tag, intents_file="intents.json"):
    """
    Retrieves a response for the given tag from the intents JSON file.
    Args:
        tag (str): The tag representing the user's query category.
        intents_file (str): Path to the JSON file containing intents (default: 'intents.json').
    Returns:
        str: A response string from the corresponding intent's responses list.
    """
    try:
        # Check if the intents file exists
        if not os.path.exists(intents_file):
            raise FileNotFoundError(f"Intents file not found at: {intents_file}")
        
        with open(intents_file, 'r') as file:
            intents = json.load(file)
        
        # Find and return a random response from the matched intent
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
        
        return "I don't understand that."
    
    except Exception as e:
        print(f"Error getting response: {e}")
        return "Sorry, I encountered an error."

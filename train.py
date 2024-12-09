import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

def load_data(file_path):
    print(f"Loading file from: {file_path}")  # Debugging line to check file path
    try:
        with open(file_path, 'r') as file:
            intents = json.load(file)
        texts, labels = [], []
        for intent in intents["intents"]:
            for pattern in intent["patterns"]:
                texts.append(pattern)
                labels.append(intent["tag"])
        return texts, labels
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}.")
        exit(1)

def train_model():
    texts, labels = load_data("intents.json")
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])
    pipeline.fit(texts, labels)
    with open('models/chatbot_model.pkl', 'wb') as model_file:
        pickle.dump(pipeline, model_file)
    print("Model trained and saved!")

if __name__ == "__main__":
    train_model()

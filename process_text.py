import os
import pandas as pd
import nltk
import json
import base64
from nltk.tokenize import word_tokenize
from flask import Flask, jsonify

nltk.download("punkt")

app = Flask(__name__)

def read_text_file(file_path):
    """Reads text from file if exists, else raises an error."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def preprocess_text(text):
    """Cleans text using Pandas and tokenizes words using NLTK."""
    df = pd.DataFrame([text], columns=["text"])
    df["text"] = df["text"].str.replace(r"\\n|\\r", " ", regex=True)
    df["text"] = df["text"].str.replace(r"\s+", " ", regex=True).str.strip()
    
    tokens = word_tokenize(df["text"][0])  # Tokenize words
    return tokens

@app.route('/get_text', methods=['GET'])
def get_text():
    """Serves processed words directly without saving files."""
    try:
        file_path = "input.txt"
        text = read_text_file(file_path)
        words = preprocess_text(text)

        # Convert to JSON and encode in Base64 to prevent file write
        json_data = json.dumps({"words": words})
        encoded_data = base64.b64encode(json_data.encode()).decode()
        
        return jsonify({"data": encoded_data})  # Frontend can decode this
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

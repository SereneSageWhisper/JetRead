import os
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from flask import Flask, Response

nltk.download("punkt")

app = Flask(__name__)

def read_text_file(file_path):
    """Reads and cleans text from a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def preprocess_text(text):
    """Cleans text and tokenizes words using NLTK."""
    df = pd.DataFrame([text], columns=["text"])
    df["text"] = df["text"].str.replace(r"\\n|\\r", " ", regex=True)
    df["text"] = df["text"].str.replace(r"\s+", " ", regex=True).str.strip()
    
    tokens = word_tokenize(df["text"][0])  # Tokenize words
    return " ".join(tokens)  # Return as space-separated words

@app.route('/get_text', methods=['GET'])
def get_text():
    """Serves processed words as plain text."""
    try:
        text = read_text_file("input.txt")
        processed_text = preprocess_text(text)
        return Response(processed_text, mimetype="text/plain")
    except Exception as e:
        return Response(str(e), status=500, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)

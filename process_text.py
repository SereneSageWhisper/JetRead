import json
import os

def read_text_file(file_path):
    """Reads a text file and handles file errors."""
    if not os.path.exists(file_path):
        print("Error: File not found.")
        return None
    
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    return text

def clean_text(text):
    """Cleans the text by removing extra spaces, handling special characters, and ensuring UTF-8 encoding."""
    text = text.replace("\n", " ").replace("\r", " ")
    text = " ".join(text.split())  # Removes extra spaces
    return text

def split_into_words(text):
    """Splits text into individual words."""
    words = text.split(" ")
    return words

def save_to_json(data, output_file="processed_text.json"):
    """Saves processed text to a JSON file for frontend use."""
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump({"words": data}, file, ensure_ascii=False, indent=2)

def main():
    file_path = "input.txt"
    text = read_text_file(file_path)

    if text:
        cleaned_text = clean_text(text)
        words = split_into_words(cleaned_text)
        save_to_json(words)
        print(f"Processed text saved to 'processed_text.json' ({len(words)} words)")

if __name__ == "__main__":
    main()

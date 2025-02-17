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

def split_into_word_pairs(text):
    """Splits text into pairs of words, handling odd numbers of words."""
    words = text.split(" ")
    pairs = [f"{words[i]} {words[i+1]}" if i+1 < len(words) else words[i] for i in range(0, len(words), 2)]
    return pairs

def save_to_json(data, output_file="processed_text.json"):
    """Saves processed text to a JSON file for frontend use."""
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump({"word_pairs": data}, file, ensure_ascii=False, indent=2)

def main():
    file_path = "input.txt"
    text = read_text_file(file_path)

    if text:
        cleaned_text = clean_text(text)
        word_pairs = split_into_word_pairs(cleaned_text)
        save_to_json(word_pairs)
        print(f"Processed text saved to 'processed_text.json' ({len(word_pairs)} word pairs)")

if __name__ == "__main__":
    main()

import pytesseract
from flask import Flask, jsonify
from PIL import Image
import os

# Define a path to the local image
local_image_path = "/home/solo/Pictures/1.png"

def extract_text_from_local_image(image_path):
    try:
        # Open the image using PIL
        with Image.open(image_path) as img:
            # Use pytesseract to extract text from the image
            extracted_text = pytesseract.image_to_string(img)

        # Check if text was detected
        if not extracted_text.strip():
            return "No text detected"

        return extracted_text

    except Exception as e:
        # Handle errors gracefully
        return f"Error: {str(e)}"

if __name__ == '__main__':
    # Extract text from the local image
    if os.path.exists(local_image_path):
        result = extract_text_from_local_image(local_image_path)
        print("Extracted Text:")
        print(result)
    else:
        print(f"Error: The file at {local_image_path} does not exist.")

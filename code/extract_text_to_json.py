from PIL import Image
import pytesseract
import json
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust this path if necessary

# Directory containing the images
image_dir = r"C:\Users\SEC\Desktop\Mini_Project\instagram_posts"  # Update this path to your image folder
# List to store each post's data
posts_data = []

# Loop over each image file in the directory
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg'):
        image_path = os.path.join(image_dir, filename)
        
        # Load image and extract text using pytesseract
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        
        # Parsing logic to extract specific fields from text
        lines = text.split('\n')
        post = {}
        for line in lines:
            line = line.strip()
            # Check for "Location:" and handle cases with leading characters
            if "Location:" in line:
                post["location"] = line.split("Location:")[1].strip()  # Get everything after "Location:"
            elif line.startswith("Issue:"):
                post["issue"] = line.replace("Issue:", "").strip()
            elif line.startswith("Description:"):
                post["description"] = line.replace("Description:", "").strip()
            elif line.startswith("Affected People:"):
                post["affected_people"] = int(line.replace("Affected People:", "").strip())
            elif line.startswith("Severity:"):
                post["severity"] = line.replace("Severity:", "").strip()
            elif line.startswith("Additional Info:"):
                post["additional_info"] = line.replace("Additional Info:", "").strip()
            elif line.startswith("Hashtags:"):
                post["hashtags"] = line.replace("Hashtags:", "").strip()
        
        # Add post data to the list if it contains information
        if post:
            posts_data.append(post)

# Save all extracted data to a JSON file
output_json_path = r"C:\Users\SEC\Desktop\Mini_Project\output_posts_data.json"  # Path to save the JSON file
with open(output_json_path, 'w') as f:
    json.dump(posts_data, f, indent=4)

print("Data has been successfully saved to", output_json_path)

import json

# Path to the JSON file
json_file_path = "/content/drive/MyDrive/Vision_LanguageFinal/MeaCap/Flickr30K/test.json"

# Open and load the JSON file
with open(json_file_path, "r") as file:
    data_dict = json.load(file)

print(len(data_dict['images']))
img_list = [i['id'] for i in data_dict['images']]
print(len(img_list))
import os
import shutil
source_dir = "/content/drive/MyDrive/Vision_LanguageFinal/MeaCap/Flickr30K/image_example/flickr30k-images"
dest_dir = ("/content/drive/MyDrive/Vision_LanguageFinal/MeaCap/image_example")
# Ensure the destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# Loop through the file IDs and copy matching files
for file_id in img_list:
    # Construct source and destination file paths
    source_file = os.path.join(source_dir, f"{file_id}.jpg")  # Assuming the files have .jpg extension
    dest_file = os.path.join(dest_dir, f"{file_id}.jpg")

    # Check if the source file exists
    if os.path.exists(source_file):
        shutil.copy(source_file, dest_file)
        print(f"Copied: {source_file} -> {dest_file}")
    else:
        print(f"File not found: {source_file}")

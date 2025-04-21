import requests
import random
import hashlib
import os

def hash_string(input_string):
    # Create a sha256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the bytes of the string (encode to bytes)
    sha256_hash.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return sha256_hash.hexdigest()

def check_file_exists(file_path):
    # Check whether the file exists in the specified folder
    return os.path.exists(file_path)

key = input('Enter a key: ')
password = input('Enter a password: ')

input_data = key + password
file_name = hash_string(input_data)

# Check if the file already exists in the 'links' folder
link_file_path = './links/' + file_name + '.txt'
if check_file_exists(link_file_path):
    # If the file exists, return its content and exit
    with open(link_file_path, 'r') as f:
        content = f.read()
        print("File already exists. Content of the file:")
        print(content)
    exit()

# Input the link of a photo
p = input('Enter a link of a photo: ')

# Try to fetch the image and handle invalid URL errors
try:
    pic = requests.get(p)
    pic.raise_for_status()  # Will raise an HTTPError for bad responses
except requests.exceptions.RequestException as e:
    print(f"Error: Invalid link or unable to retrieve the image. {e}")
    exit()

# Save the link to the 'links' folder
os.makedirs('./links', exist_ok=True)  # Ensure the folder exists
with open(link_file_path, 'a') as f:
    f.write(p + '\n')

# Save the picture to the 'pics' folder
os.makedirs('./pics', exist_ok=True)  # Ensure the folder exists
pic_file_path = './pics/' + file_name + '.jpg'
with open(pic_file_path, 'wb+') as f:
    f.write(pic.content)

print(f"Link and picture have been saved successfully.\nLink saved in: {link_file_path}\nPicture saved in: {pic_file_path}")

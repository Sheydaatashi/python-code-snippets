import requests
import hashlib
import os

def hash_string(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def check_file_exists(file_path):
    return os.path.exists(file_path)

def main():
    key = input('Enter a key: ')
    password = input('Enter a password: ')

    input_data = key + password
    file_name = hash_string(input_data)

    link_file_path = '../data/links/' + file_name + '.txt'
    if check_file_exists(link_file_path):
        with open(link_file_path, 'r') as f:
            content = f.read()
            print("File already exists. Content of the file:")
            print(content)
        exit()

    p = input('Enter a link of a photo: ')

    try:
        pic = requests.get(p)
    except requests.exceptions.RequestException as e:
        print(f"Error: Invalid link or unable to retrieve the image. {e}")
        exit()

    with open(link_file_path, 'a') as f:
        f.write(p + '\n')

    pic_file_path = '../data/pics/' + file_name + '.jpg'
    with open(pic_file_path, 'wb+') as f:
        f.write(pic.content)

    print(f"Link and picture have been saved successfully.\nLink saved in: {link_file_path}\nPicture saved in: {pic_file_path}")

if __name__ == "__main__":
    main()

file_path = input("Enter the file name: ")

try:
    with open(file_path, 'r') as file:
        text = file.read()
except:
    print("Could not read the file!")
    exit()

words = text.lower().split()
clean_words = []

for word in words:
    clean_word = ""
    for letter in word:
        if letter.isalpha():
            clean_word += letter
    if clean_word:
        clean_words.append(clean_word)

word_count = {}
for word in clean_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

total_words = len(clean_words)
total_chars = len(text.replace(" ", ""))

print(f"\nTotal words: {total_words}")
print(f"Total characters (no spaces): {total_chars}")
print("\nMost common words:")

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:10]:
    print(f"{word}: {count}")

with open('results.txt', 'w') as file:
    file.write(f"Total words: {total_words}\n")
    file.write(f"Total characters (no spaces): {total_chars}\n")
    file.write("\nMost common words:\n")
    for word, count in sorted_words[:10]:
        file.write(f"{word}: {count}\n")

print("\nResults saved to 'results.txt'")
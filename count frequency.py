# word_frequency.py

import string

def count_word_frequency(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Split into words
    words = text.split()

    # Initialize dictionary
    word_freq = {}

    # Count words
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


def main():
    print("Enter a block of text:")
    text = input("> ")

    frequency = count_word_frequency(text)

    print("\nWord Frequency:\n")
    for word in sorted(frequency):
        print(f"{word}: {frequency[word]}")


if __name__ == "__main__":
    main()

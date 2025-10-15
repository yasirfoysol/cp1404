"""
CP1404 | Practical 05 | Word Occurrences
Estimate: 25 minutes
Actual:   22 minutes
"""

def main():
    """Count the occurrences of words in a given text."""
    text = input("Text: ")
    words = text.split()
    word_to_count = {}
    for word in words:
        word = word.lower()
        word_to_count[word] = word_to_count.get(word, 0) + 1

    words = sorted(word_to_count.keys())
    longest_word_length = max(len(word) for word in words)
    for word in words:
        print(f"{word:{longest_word_length}} : {word_to_count[word]}")


if __name__ == "__main__":
    main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_counts = count_characters(text)
    print_report(book_path, word_count, character_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_counts = {}
    for char in text:
        if char.isalpha():  # Considering only alphabetic characters
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts

def print_report(path, word_count, character_counts):
    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main()

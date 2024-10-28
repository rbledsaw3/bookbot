def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')

def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        print(f"Total words: {len(words)}")

def count_characters(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        char_set = set(text)
        char_counts = {char: text.count(char) for char in char_set}
    return char_counts

def main():
    file_path = "books/frankenstein.txt"
    read_file(file_path)
    count_words(file_path)
    print(count_characters(file_path))


if __name__ == "__main__":
    main()


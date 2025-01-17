def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')

def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        return len(words)

def count_characters(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        char_set = set(text)
        char_counts = {char: text.count(char) for char in char_set}
        sorted_char_counts = dict(sorted(char_counts.items()))
    return sorted_char_counts

def report(file_path):
    word_count = count_words(file_path)
    char_counts = count_characters(file_path)
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print("\n")
    for char, count in char_counts.items():
        if char == '\n':
            char = 'newline'
        elif char == ' ':
            char = 'space'
        elif char == '\t':
            char = 'tab'
        elif char == '\r':
            char = 'carriage return'
        elif char == '\v':
            char = 'vertical tab'
        elif char == '\f':
            char = 'form feed'
        print(f"The \'{char}\' character was found {count} times")
    print("--- End report ---")


def main():
    file_path = "books/frankenstein.txt"
    report(file_path)
    


if __name__ == "__main__":
    main()


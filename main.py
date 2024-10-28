def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')

def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        print(f"Total words: {len(words)}")

def main():
    file_path = "books/frankenstein.txt"
    read_file(file_path)
    count_words(file_path)


if __name__ == "__main__":
    main()


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

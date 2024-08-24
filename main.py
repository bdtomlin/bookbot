def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_header(book_path)
    print_word_count(text)
    print_new_line()
    print_alpha_char_counts(text)
    print_new_line()
    print_footer()

def print_header(path):
    print(f"--- Begin report for {path} ---")

def print_word_count(text):
    print(f"{word_count(text)} words found.")

def print_new_line():
    print("\n")

def print_alpha_char_counts(text):
    for item in alpha_list(text):
        char = item["char"]
        count = item["count"]
        print(f"The '{char}' character was found {count} times")

def print_footer():
    print("--- End report ---")

# ------------- supporting functions -------------

def alpha_list(text):
    char_counts = character_counts(text)
    alpha_dict = filter_alpha(char_counts)
    sorted_list = sorted_count_list(alpha_dict)
    return sorted_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


def filter_alpha(char_counts):
    alpha_dict = {}
    for c in char_counts:
        if c.isalpha():
            alpha_dict[c] = char_counts[c]
    return alpha_dict

def sort_on(dict):
    return dict["count"]

def sorted_count_list(count_dict):
    count_list = []
    for k in count_dict:
        count_list.append({"char": k, "count": count_dict[k]})
    count_list.sort(reverse=True, key=sort_on)
    return count_list


def word_count(text):
    words = text.split()
    return len(words)

def character_counts(text):
    counts = {}
    for c in text.lower():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

main()

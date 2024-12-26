def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_num_words(text)
    num_char = count_num_chars(text)
    list_of_char = dict_to_list(num_char)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for dict in list_of_char:
        if dict["char"].isalpha():
            print(f"The '{dict["char"]}' character was found {dict["num"]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_num_words(text):
    words = text.split()
    return len(words)
    
def count_num_chars(text):
    words = text.split()
    num_chars = dict()
    for word in words:
        for char in word:
            if char.lower() in num_chars:
                num_chars[char.lower()] += 1
            else:
                num_chars[char.lower()] = 1
    return num_chars

def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    list_of_char =[]
    for key in dict:
        list_of_char.append({"char": key, "num": dict[key]})
    list_of_char.sort(reverse = True, key=sort_on)
    return list_of_char


main()
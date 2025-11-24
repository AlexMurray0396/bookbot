def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    list = text.split()
    word_count = len(list)
    return word_count

def get_word_count(book):
    count = word_count(book)

    return count

def get_character_counts(book):
    book_lower = book.lower()

    count_dict = {}

    for char in book_lower:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    
    return count_dict

def sort_on(items):
    return items["num"]

def dict_list(dict):
    dict_list = []

    for item in dict:
        inner_dict = {}
        inner_dict["char"] = item
        inner_dict["num"] = dict[item]
        dict_list.append(inner_dict)
    
    dict_list.sort(reverse = True, key = sort_on)

    return dict_list

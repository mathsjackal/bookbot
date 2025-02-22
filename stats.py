# Statistics on books
def get_num_words(contents):
    word_list = contents.split()
    word_count = len(word_list)
    return word_count

def char_count(contents):
    char_dict = {}
    contents = contents.lower()
    for char in contents:
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(dictionary):
    char_list = list(dictionary.items())
    char_list.sort(key=lambda item: item[1], reverse=True)
    sorted_char_dict = dict(char_list)
    filtered_char_dict = {}
    for char, count in sorted_char_dict.items():
        if char.isalpha():
            filtered_char_dict[char] = count
    return filtered_char_dict


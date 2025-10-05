#
#
# Function to count the words in the file
def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

# Function to count characters and return a
# dictionary of those characters and list
def char_count(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] = 1
    
    return char_dict

#
# Helper function for sorting lists
def sort_on(items):
    return items["num"]
#
# This function is going to take the dictionary of values and return two sorted lists. 
def sort_lists(char_dict):
    scr_list = []
    scr_dict = {}
    for key,value in char_dict.items():
        scr_dict = {"char": key, "num": value}
        scr_list.append(scr_dict)
    
    scr_list.sort(reverse=True, key=sort_on)

    return scr_list


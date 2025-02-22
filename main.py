# Bookbot main file.
# 

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    import sys
    from stats import get_num_words
    from stats import char_count
    from stats import sort_dict   
    num_args = len(sys.argv)
    if num_args != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
 #       print(sys.argv[1])
    content = get_book_text(file_path)
    word_count = get_num_words(content)
    char_dict = char_count(content)
    sorted_dict = sort_dict(char_dict)
    #print(f"{word_count} words found in the document")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char,count in sorted_dict.items():
        print(f"{char}: {count}")
    print("============= END ===============")
main()
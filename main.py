# Bookbot 
#
# Get stats function from stats.py
from stats import count_words, char_count, sort_lists
import sys
#
#
# Get Book Text Function:
def get_book_text(file_path):
    try:
        with open(file_path, "r") as file:
            book_string = file.read()
        return book_string
    except FileNotFoundError:
        print("Invalid file path.") 

    


def main():
    
    #file_location = input("Enter book location.")
 #   file_location = './books/frankenstein.txt'
    if len(sys.argv) ==1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    file_location = sys.argv[1]

    book_text = get_book_text(file_location)
    total_count = count_words(book_text)
    char_sum = char_count(book_text)
    
    list_scr = sort_lists(char_sum)
    #print(sys.argv)
    # Format output per orders
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_count} total words")
    print("--------- Character Count -------")
    for item in list_scr:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()



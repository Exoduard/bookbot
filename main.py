from stats import count_words, count_characters, sort_dictionary
import sys
# This code reads a book from a file and counts the number of words in it.

def get_book_text(filename):
    with open(filename, "r") as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filename = sys.argv[1]
    if not filename.endswith('.txt'):
        print("Please provide a valid text file.")
        sys.exit(1)
        
    text = get_book_text(filename)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n")
    print("----------- Word Count ----------")
    count_words(text)
    print("--------- Character Count -------")
    dict_frank = count_characters(text)
    sorted_dict = sort_dictionary(dict_frank)
    
    for char, count in sorted_dict.items():
        print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()

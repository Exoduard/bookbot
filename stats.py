def count_words(text):
    words = text.split()
    return print(f"Found {len(words)} total words")

def count_characters(text):
    lower = text.lower()
    dict_frank = {}
    for char in lower:
        if char.isalpha():
            if char in dict_frank:
                dict_frank[char] += 1
            else:
                dict_frank[char] = 1
    return dict_frank
    
def sort_dictionary(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
    
    
def report(dictionary, count):
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------")
    count_words(count)
    print("--------- Character Count -------")
    for char, count in dictionary.items():
        print(f"{char}: {count}")
    return dictionary
    print("============= END ===============")
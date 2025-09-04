import sys
from stats import get_book_text, number_of_characters, sorter

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    counts = number_of_characters(text)
    sorted_chars = sorter(counts)
    words = text.split()
    print("============ BOOKBOT ============ ")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")
    

if __name__ == "__main__":
    main()

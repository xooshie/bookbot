from stats import get_num_words, get_chars_dict, dict_to_list_of_dicts
import sys

def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents
  

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text.lower())
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    list = dict_to_list_of_dicts(chars_dict)
    for i in range(0, len(list)):
        if list[i]['char'].isalpha():
          print(f"{list[i]['char']}: {list[i]['num']}")

    print("============= END ===============")
  
  

main()
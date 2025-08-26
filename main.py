from stats import count_words_in_text, count_characters_in_text, sorted_character_count
import sys

TITLE = "============ BOOKBOT ============"
WORD_COUNT = "----------- Word Count ----------"
CHARACTER_COUNT = "--------- Character Count -------"
END = "============= END ==============="

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    print(TITLE)
    print(f"Analyzing book found at {filepath}...")
    print(WORD_COUNT)
    num_words = count_words_in_text(filepath)
    print(f"Found {num_words} total words")
    print(CHARACTER_COUNT)
    character_count_dict = count_characters_in_text(filepath)
    sorted_list = sorted_character_count(character_count_dict)
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print(END)

main()

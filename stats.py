def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def count_words_in_text(filepath: str) -> int:
    book_text = get_book_text(filepath)
    return len(book_text.split())

def count_characters_in_text(filepath: str) -> dict:
    book_text = get_book_text(filepath)
    book_text_lower = book_text.lower()
    character_count_dict = {}
    for character in book_text_lower:
        if character in character_count_dict:
            character_count_dict[character] += 1
        else:
            character_count_dict[character] = 1
    return character_count_dict

def sorted_character_count(character_count: dict) -> list:
    character_count_list = []
    for k, v in character_count.items():
        character_count_list.append({"char": k, "num": v})
    def sort_on(items):
        return items["num"]
    character_count_list.sort(reverse = True, key = sort_on)
    return character_count_list

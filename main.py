def word_in_book(book_text: str) -> int:
    number_of_words = len(book_text.split())
    return number_of_words

def get_character_occurences(book_text: str):
    character_map = {}
    for character in book_text:
        character = character.lower()
        
        if character_map.get(character) != None:
            character_map[character] += 1
        else:
            character_map.update({character: 1})
    
    return character_map

def print_report(book_text: str):
    print("--- Begin report of books/frankenstein.txt ---")
    words_in_book = word_in_book(book_text)
    print(f"{words_in_book} words found in the document")
    print("")
    character_dict = get_character_occurences(book_text)
    temp = "fd"
    for key, val in character_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {val} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print_report(file_content)
        


main()
import string

def main():
    book_path = "books/frakenstein.txt"
    file_contents = read_book(book_path)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    sorted_char_count = sort_dict(char_count)
    report = generate_report(book_path, word_count, sorted_char_count)
    
    print(report)
        
def read_book(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    char_dict = {}
    
    for word in text:
        if word not in string.ascii_letters:
            continue
        
        lowered_word = word.lower()
        
        if lowered_word not in char_dict:
            char_dict[lowered_word] = 1
        else:
            char_dict[lowered_word] += 1
            
    return char_dict

def sort_dict(dict): 
    characters = []
       
    for key in dict:
        character = {
            "name": key,
            "num": dict[key]
        }
        
        characters.append(character)
    
    characters.sort(reverse=True, key=sort_on)
    return characters
    
def sort_on(dict):
    return dict["num"]   

def generate_report(book_path, word_count, sorted_char_count):
    report = ""
    
    report += f"--- Begin report of {book_path} ---\n"
    report += f"{word_count} words found in the document\n\n"
    
    for char in sorted_char_count:
        word = char["name"]
        count = char["num"]
        
        report += f"The '{word}' character was found {count} times\n"
        
    report += "--- End report ---"
    
    return report

        
main()
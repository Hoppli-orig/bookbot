def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    
    total_words = 0
    words = file_contents.split()
    for k in words:
        total_words += 1

    letters = {} 
    lower_file_contents = file_contents.lower()
    for char in lower_file_contents:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    sorted_items = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    for char, count in sorted_items:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")



if __name__=="__main__":
    main()
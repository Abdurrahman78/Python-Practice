#implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

def vowelRemover():
    text=input("Input: ")
    newText=""
    for char in range(len(text)):
        if text[char].capitalize() != 'A' and text[char].capitalize() != 'E' and  text[char].capitalize() != 'I' and text[char].capitalize() != 'O' and text[char].capitalize() != 'U':
            newText+=text[char]

    print(f"Output: {newText}")


vowelRemover()

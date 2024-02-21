def main():
    value=shorten(input("Input: "))
    print(value)


def shorten(word):
    newText=""
    for char in range(len(word)):
        if word[char].capitalize() != 'A' and word[char].capitalize() != 'E' and  word[char].capitalize() != 'I' and word[char].capitalize() != 'O' and word[char].capitalize() != 'U':
            newText+=word[char]
    return newText


if __name__ == "__main__":
    main()

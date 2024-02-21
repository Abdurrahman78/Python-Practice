#implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case

def main():
    answer=camelToSnake(input("camelCase: "))
    print(f"snake_case: {answer}")

def camelToSnake(word):
    newWord=""
    for index in range(len(word)):
        if word[index].isupper():
            newWord+="_" + word[index].lower()
        else:
            newWord+=word[index]

    return newWord


main()

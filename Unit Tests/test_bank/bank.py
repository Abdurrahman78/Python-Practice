def main():
    value1=value(input("Greeting: "))
    print(value1)

def value(greeting):
        #If the greeting starts with “hello” or if scetence starts with hello
    if greeting.strip().lower() == "hello" or greeting.strip().lower().startswith("hello"):
        return 0

    #If the greeting starts with an “h” (but not “hello”)
    elif (greeting.strip().lower() != "hello") and (greeting.strip().lower()[0:1]=='h') :
        return 20

    #Otherwise, output $100.
    else:
        return 100


if __name__ == "__main__":
    main()

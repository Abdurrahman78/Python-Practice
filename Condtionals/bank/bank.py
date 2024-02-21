#implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
#Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.


# prompts the user for a greeting
greeting=input('Greeting: ')

#If the greeting starts with “hello” or if scetence starts with hello
if greeting.strip().lower() == "hello" or greeting.strip().lower().startswith("hello"):
    print('$0')

#If the greeting starts with an “h” (but not “hello”)
elif (greeting.strip().lower() != "hello") and (greeting.strip().lower()[0:1]=='h') :
    print('$20')

#Otherwise, output $100.
else:
    print('$100')

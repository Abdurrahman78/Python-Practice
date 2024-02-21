#implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
#Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
# No need to pluralize the items. Treat the user’s input case-insensitively.

new_Dic={
}
counter=1
while True:
    try:
        food=input().upper()
        if food in new_Dic:
            new_Dic[food]+=1
        else:
            new_Dic[food]=counter
    except KeyError:
        pass
    except EOFError:
        print("\n")
        for key in sorted(new_Dic):
            print(new_Dic[key],key)
        break


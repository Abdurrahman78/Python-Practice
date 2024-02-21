#implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names,
#separating two names with one and, three names with two commas and one and, and
#  names with
#  commas and one and, as in the below:





import inflect
p = inflect.engine()
list=[]
while True:
    try:
        answer=input("Name: ")
        list.append(answer)
        print(list)
    except EOFError:
        mylist=p.join(list)
        print(f"Adieu, adieu, to {mylist} ")
        break



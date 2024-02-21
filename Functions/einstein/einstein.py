#implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
#Assume that the user will input an integer.


def massConverter():
    #prompts the user for mass as an integer
    mass=int(input("M: "))
    #outputs the equivalent number of Joules as an integer
    print(pow(300000000,2)*mass)





massConverter()

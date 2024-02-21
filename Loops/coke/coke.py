#implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
#Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers,
#and ignore any integer that isn’t an accepted denomination.

def amountDue():
    amount=50
    while amount>0:
        print(f"Amount Due: {amount}")
        moneyGiven=int(input("Insert Coin: "))
        if moneyGiven in (25,10,5):
            amount=amount-moneyGiven
            continue
    change=abs(amount)
    print(f"Change Owed: {change}")



amountDue()


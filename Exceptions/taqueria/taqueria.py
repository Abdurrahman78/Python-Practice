dictionary={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total=0
newDictionary={}

for key in dictionary:
    newDictionary[key.lower()]=dictionary[key]


while True:
    try:
        item=input("Item: ").lower()
        total+=newDictionary[item]

        print(f"Total: ${total:.2f}")
    except KeyError:
        pass
    except EOFError:
        print("\n")
        break



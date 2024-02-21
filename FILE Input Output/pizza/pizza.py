import sys
import csv
from tabulate import tabulate

def printTable():

    if len(sys.argv)==1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv)>2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        fileName=sys.argv[1]
        extensionName=fileName[-4:]
        if extensionName != ".csv":
            print("Not a CSV file")
            sys.exit(1)
        else:
            try:
                table=[]
                with open(sys.argv[1]) as file:
                    lines=csv.reader(file)
                    for line in lines:
                        table.append([line[0],line[1],line[2]])
                headers=table[0]
                table.pop(0)
                print(tabulate(table,headers,tablefmt="grid"))
            except FileNotFoundError:
                    print("File does not exist")
                    sys.exit(1)

printTable()

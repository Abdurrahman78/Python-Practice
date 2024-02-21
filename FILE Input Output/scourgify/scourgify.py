import csv
import sys

if len(sys.argv)<3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv)>3:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    try:
        newFile=[]
        with open(sys.argv[1]) as file:
            reader=csv.DictReader(file)
            for row in reader:
                last,first1=row["name"].split(",")
                first=first1.lstrip()
                newFile.append({"first":first,"last":last,"house":row["house"]})

        fieldname=["first","last","house"]

        with open(sys.argv[2],"w") as newFile1:
            writer=csv.DictWriter(newFile1, fieldnames=fieldname)

            writer.writeheader()

            for row in newFile:
                writer.writerow(row)


    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]} ")
        sys.exit(1)


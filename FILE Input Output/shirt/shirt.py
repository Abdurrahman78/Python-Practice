import sys
from PIL import Image,ImageOps
import os

if len(sys.argv)<3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv)>3:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    validValues=(".jpg","jpeg",".png")
    extension1=os.path.splitext(sys.argv[1])[1].lower()
    extension2=os.path.splitext(sys.argv[2])[1].lower()
    if extension1 not in validValues or extension2 not in validValues:
        print("Invalid Input")
        sys.exit(1)
    elif extension1 != extension2:
        print("Input and output have different extensions")
        sys.exit(1)
    else:
        try:
            originalPhoto=Image.open(sys.argv[1])
            shirt=Image.open("shirt.png")
            shirtWH=shirt.size
            resizedPhoto=ImageOps.fit(originalPhoto,shirtWH)
            resizedPhoto.paste(shirt,mask=shirt)
            resizedPhoto.save(sys.argv[2])


        except FileNotFoundError:
            print("Input File does not exist")
            sys.exit(1)






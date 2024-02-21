#implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip

#If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default

fileName=input('File name: ').strip().lower()

newfileName=fileName.split(".")

if (newfileName[len(newfileName)-1]) == 'txt':
    answer='txt'
    specialAnswer=newfileName[0]

elif len(newfileName)>1:
    answer=newfileName[len(newfileName)-1]

else:
    answer=newfileName[0]


match answer:
    case "gif" | "png":
        print(f"image/{answer}")
    case  "jpg" | "jpeg":
        print("image/jpeg")
    case "txt":
        print(f"text/{specialAnswer}")
    case "zip" | "pdf":
        print(f"application/{answer}")
    case _:
         print("application/octet-stream")



import sys

def countLines():

    if len(sys.argv)==1:
        sys.exit(1)
    elif len(sys.argv)>2:
        sys.exit(1)
    else:
        fileName=sys.argv[1]
        extensionName=fileName[-3:]
        if extensionName != ".py":
            sys.exit(1)
        else:
            try:
                count=0
                list=[]
                with open(sys.argv[1],"r") as file:
                    lines=file.readlines()
                    for line in lines:
                        list.append(line.lstrip())
                for sentence in list:
                    if sentence.startswith('#') or sentence=='':
                        continue
                    else:
                        count+=1
                return count
            except FileNotFoundError:
                    print("File does not exist")


print(countLines())

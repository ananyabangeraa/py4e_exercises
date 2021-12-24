count = 0
filename = input("Enter a filename with .txt extension:")
if(filename == "na na boo boo"):
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    exit()
try:
    fhand = open(filename)
    for line in fhand:
        if line.startswith("Author:"):
            count = count +1
        else:
            continue
    print("There were",count,"authors in",filename)
except:
    print("File cannot be opened:",filename)

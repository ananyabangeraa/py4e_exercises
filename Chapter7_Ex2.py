count = 0
y = 0
try:
    fhand = open("mbox-short.txt")
    #print(fhand)
    for line in fhand:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence"):
            index = line.find("0")
            x = float(line[index:])
            y = y + x
            count = count + 1
        else:
            continue
    print("Average spam confidence:",(y/count))    
except:
    print("Invalid file type!")

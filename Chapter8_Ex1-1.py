list1 = list()
try:
    fhand = open("C:\\Users\\Lenovo\\Desktop\\Python Exercises\\ana.txt")
    for line in fhand:
        line = line.split()
        for word in line:
            if word not in list1:
                list1.append(word)
            else:
                continue
    print(list1)
    list1.sort()
    # list1.sort(reverse=-1)
    for elements in list1:
        print(elements)
except:
    print("File does not exist!")


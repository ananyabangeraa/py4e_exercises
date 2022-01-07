# list1 = list()
# try:
#     fhand = open("C:\\Users\\Lenovo\\Desktop\\Python Exercises\\mbox-short.txt")
#     for line in fhand:
#         if line.startswith('From:'):
#             if line[5:] not in list1:
#                 list1.append(line[5:])
#     for elements in list1:
#         print(elements)       
# except:
#     print("Didn't work!")          
try:
    fhand = open("C:\\Users\\Lenovo\\Desktop\\Python Exercises\\mbox-short.txt")
    print("Opened file")
    for line in fhand:
        if line.startswith("From:"):
            count = count+1
            line = line.split()
            print(line[1])
    print("There were",count,"many lines in the file with From as the first word.")

except:
    print("Error")

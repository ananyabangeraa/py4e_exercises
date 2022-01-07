list1 = list()
while(1):
    l = input("Enter a number:")
    if l != "done":
        list1.append(float(l))
    else:
        break
print("Entered list is:",list1)
print("Maximum:",max(list1))
print("Minimum:",min(list1))


    
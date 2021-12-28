def chop(list1):
    del list1[0]
    del list1[-1]
    return None
def middle(list2):
    list3 = list2[1:-1]
    return list2
list1 = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    list1.append(value)
#list1 = [1,2,3,4,5]
print("The original list is:",list1)
print(chop(list1))
print(middle(list1))
    

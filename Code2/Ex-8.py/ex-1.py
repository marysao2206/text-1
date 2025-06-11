def removeNumSeven(list):
    myNewList = []
    for num in list:
        if num != 7:
            myNewList.append(num)
    return myNewList

myArray = [1,2,5,6,7,0,2,7,8,9]
result = removeNumSeven(myArray)
print(result)

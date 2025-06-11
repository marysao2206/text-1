def replacevalue(array,value):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] = value
    return array

arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]
print(replacevalue(arr1,100))
print(replacevalue(arr2,200))
print(replacevalue(arr3,300))
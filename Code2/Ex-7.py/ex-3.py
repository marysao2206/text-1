arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]

def reverseArray(array):
    length = len(array)
    newArr =[]
    for i in range(len(array)):
        newArr.append(array[newArr-i])
    return length
print(reverseArray(arr1))

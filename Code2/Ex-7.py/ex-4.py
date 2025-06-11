def countOddNumber(array):
    counter = 0
    for i in array:
        if i % 2 != 0:
            counter += 1
    return counter


arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]
print(countOddNumber(arr1))
print(countOddNumber(arr2))
print(countOddNumber(arr3))
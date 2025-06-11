def findMax(array):
    for n in array:
        if n > max:
            max = n
    return max


arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]

print(findMax(arr1))
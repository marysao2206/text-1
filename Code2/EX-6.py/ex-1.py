def sumarray(array):
    sum=0
    for num in array:
        sum+=sum
    return(sum)
arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]
print(sumarray(arr1))
print(sumarray(arr2))
print(sumarray(arr3))
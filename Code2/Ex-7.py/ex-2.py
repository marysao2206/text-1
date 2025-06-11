arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]

def minimum (array):
    sum = 0
    for value in arr2:
        if value % 2== 0:
            sum+=value
    return sum
print(minimum(arr2))

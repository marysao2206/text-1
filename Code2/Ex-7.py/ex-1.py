arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]

def minimum (array):
    min = array[0]
    for i in array:
        if i < min:
         min = i
    return(min)
print(minimum(arr1))
print(minimum(arr2))
print(minimum(arr3))





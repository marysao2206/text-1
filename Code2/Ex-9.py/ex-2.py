array = [2, 4, 5, 7, 3, 9, 1]
    # #1 - Find maximum and minimum value from this array and sum them together
def sum(array):
    min_number = array[0]
    max_number = array[0]
    for i in range(len(array)):
        if (array[i]) < min_number:
            min_number = array[i]
        if (array[i]) > max_number:
            max_number = array[i]
            sum = min_number + max_number
    return sum
array = [2, 4, 5, 7, 3, 9, 1]
print(sum(array))
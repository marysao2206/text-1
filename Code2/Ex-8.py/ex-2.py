# myArray = [1,2,5,6,7,9,2,7,8,9]
# def indexSeven(array):
#     for i in range(len(array)):
#         if array[i]==7:
#            myArray.append(i)
#     return indexSeven
# print(indexSeven)
        

def numSeven(numbers):
    
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] == 7:
            sum += 1
    return sum
numbers = [3, 7, 8, 7, 9, 7]    
print(numSeven(numbers)) 

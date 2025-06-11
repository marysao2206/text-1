numbers = [2, 3, 4, 5, 6, 7, 3, 8, 9, 3, 1]
newNumbers = []
lastIndex = len(numbers) - 1
for i in range(len(numbers)):
  newNumbers.append(numbers[lastIndex - i])
print(newNumbers)
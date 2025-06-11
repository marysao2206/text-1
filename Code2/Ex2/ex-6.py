numbers = [2, 3, 4, 5, 6, 7, 3, 8, 9, 3, 1]
i=0
isFirstThree=False
while i<len(numbers) and not isFirstThree:
    if numbers[i] ==3:
     print(i)
isFirstThree=True
i += 1
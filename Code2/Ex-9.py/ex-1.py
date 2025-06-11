String= ("1 2 6 3 4 0 5")
def min_number(string):
    min_number =string
    for i in range(len(string)):
        if string[i]!=" ":
            if (string[i])<min_number:
                min_number=string[i]
    return min_number
string_number = "1 2 6 3 4 0 5"
print(min_number(string_number))

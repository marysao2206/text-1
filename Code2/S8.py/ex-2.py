numbers=int(input("enter a number"))
if numbers % 2 == 0 and numbers>0:
    print("Your enter is even and positive number")
elif numbers % 2 == 0 and numbers<0:
    print("Your enter is even and negative number")
elif numbers % 2 != 0 and numbers>0:
    print("Your enter is odd and positive number")
elif numbers % 2 != 0 and numbers<0:
    print("Your enter is odd and negative number")
else:
    print("Your enter the center nmber(0)")

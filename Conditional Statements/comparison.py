#Asking the user for the value
n = float(input("Enter the value="))
#Declaring the variables
increment=0
decrement=0
#Giving the condition
if (n>15):
    increment=(n-15)
    print(f"{n} is more than 15 by {increment}.")
else:
    decrement=(15-n)
    print(f"{n} is less than 15 by {decrement}.")
    
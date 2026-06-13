a=int(input("Enter the first value="))
b=int(input("Enter the second value="))
c=int(input("Enter the third value="))
#Value of a is being given to b
#Value of b is being given to c
#Value of c is being given to a
print(f"Before swapping: a={a} b={b} c={c}")
temp=c
c=b
b=a
a=temp
print(f"After swapping: a={a} b={b} c={c}")




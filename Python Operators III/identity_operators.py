x=int(input("Enter a value="))
if(type(x) is int):
    print(f"{x} is an integer.")
else:
    print(f"{x} is not an integer.")
y=float(input("Enter a value="))
if (type(y) is not float):
    print(f"{y} is not a decimal value.")
else:
    print(f"{y} is a decimal value.")
a=int(input("Enter a value="))
b=int(input("Enter a value="))
c=b
if a is b:
    print(f"{a} and {b} are the same objects")
elif (a==b):
    print(f"{a} and {b} are identical but not same.")
else:
    print(f"{a} and {b} are completely different.")
if c is not b:
    print(f"{c} and {b} are not identical.")
else:
    print(f"{c} and {b} are the same object.")
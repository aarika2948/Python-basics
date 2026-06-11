#Taking input for the character from the user
alpha=input("Enter a character=").lower()
bet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
if alpha in bet:
    print(f"{alpha} is an alphabet.")
else:
    print(f"{alpha} is not an alphabet.")
#or
alphab=input("Enter a character=")
if(alphab.isalpha()):
    print(f"{alphab} is an alphabet.")
else:
    print(f"{alphab} is not an alphabet.")


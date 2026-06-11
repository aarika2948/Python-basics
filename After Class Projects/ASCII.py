#take the input of the character from the user
char=input("Enter any charcter=")
#Checking validity
if (type(char) is str) and (len(char)==1):
    print("Valid Input")
else:
    print("Invalid input, Enter only ONE character")
    char=input("Enter any charcter=")
#Displaying the ASCIIN value
code=ord(char)
print(f"The ASCII of {char} is {code}.")
#Converting the ASCII back
print("For verification purposes:")
code_2=int(input("Enter the ASCII code displayed earlier="))
char_2=chr(code_2)
if (char_2==char):
    print(f"The character for the ASCII code {code_2} is {char_2}")
    print("Thus, the result is absolutely correct.")
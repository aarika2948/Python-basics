#Introduction Statement
print("Hi, I am Raj. Here is a list of my friends:- \n Aaradhya \n Kimaya \n Deeva \n Tithi \n Sharini")
print(" You can enter the name of whichever friend of mine's birthday you wish to know")
print
AARADHYA = "25th March"
KIMAYA = "4th November"
DEEVA = "18th October"
TITHI = "4th Novemeber"
SHARINI = "9th February"
f_1 = "aaradhya"
f_2 = "kimaya"
f_3 = "deeva"
f_4 = "tithi"
f_5 = "sharini"
name=input("Enter the name=").lower()
if name == f_1:
    print(f"{f_1}'s birthday is on {AARADHYA}.")
elif name == f_2:
    print(f"{f_2}'s birthday is on {KIMAYA}.")
elif name == f_3:
    print(f"{f_3}'s birthday is on {DEEVA}.")
elif name == f_4:
    print(f"{f_4}'s birthday is on {TITHI}.")
elif name == f_5:
    print(f"{f_5}'s birthday is on {SHARINI}.")
else:
    print("Invalid Input.")
     


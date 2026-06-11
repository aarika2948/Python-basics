#Taking the marks as an input for various subjects
maths=float(input("Enter your marks in maths="))
science=float(input("Enter your marks in science="))
english=float(input("Enter your marks in english="))
computer=float(input("Enter your marks in computer="))
french=float(input("Enter your marks in french="))
#Taking the maximum marks
total=int(input("Enter the maximum marks of each subject="))
#Calculating the average
tot=(maths + science+ english + computer + french)
avg= int(tot/5)
#Declaring the valid range
validRange=range(1, total+1)
#Giving the condition
if avg not in validRange:
    print("Invalid Input!")
elif avg in range(91, 100):
    print("Your grade is A+")
elif avg in range(75, 90):
    print("Your grade is A")
elif avg in range(60, 74):
    print("Your grade is B")
elif avg in range(50, 59):
    print("Your grade is C")
elif avg in range(35, 49):
    print("Your grade is D")
else:
    print("You have failed.")
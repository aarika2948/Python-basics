#Take the height and weight from the user
weight=float(input("Enter your weight="))
height=float(input("Enter your height="))
#Calculate the BMI
BMI= weight / (height/100)**2
print("Your BMI is", round(BMI,2))
#Display the health
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are over weight")
elif BMI <= 34.9:
    print("You are severly overweight.")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severly obese")
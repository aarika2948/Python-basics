#Asking the user for temperature
temp = float(input("Enter the temperature in Celcius="))
#Giving conditions
if (temp<=20):
    print(f"You must wear slightly warn clothing as the temperature is {temp} degree")
else:
    print(f"You must wear light clothing as the temperature is {temp} degree.")
    
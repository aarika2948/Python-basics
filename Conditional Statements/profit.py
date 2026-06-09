#Asking the user for the values
cp=float(input("Enter the cost price of the article="))
sp=float(input("Enter the selling price of the article="))
#Declaring the variables
profit = 0
loss = 0
#Giving the condition
if (sp>cp):
    profit=(sp-cp)
    print(f"The article was sold at a profit of Rs.{profit}")
else:
    loss=(cp-sp)
    print(f"The article was sold at a loss of Rs.{loss}")

    


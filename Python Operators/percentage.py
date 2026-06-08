#Asking the user for the total no. of marks for each subject
max=int(input("Enter the maximum no. of marks that can be obtained="))
#Asking the user for the maeks of each subject
english=int(input("Enter the marks obtained in English="))
maths=int(input("Enter the marks obtained in Maths="))
computer=int(input("Enter the marks obtained in Computer="))
science=int(input("Enter the marks obtained in Science="))
#Calculating the percentage
total_max=(max*4)
total=(english+maths+computer+science)
percentage=(total*100)/total_max
#Displaying the perecntage
print(f"The perecntage after scoring the marks of {english} in English, {maths} in Maths, {computer} in Computer and {science} in Science is {percentage}%")

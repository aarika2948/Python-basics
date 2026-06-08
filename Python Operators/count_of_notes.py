#Asking for the amount from the user
amount=int(input("Enter the value="))
#Calculating the no. of notes
note_hundred=(amount//100)
note_fifty=(amount%100)//50
note_ten=((amount%100)%50)//10
#Diplaying the no. of notes initially calculated
print(f"There will be {note_hundred} notes of Rs.100")
print(f"There will be {note_fifty} notes of Rs.50")
print(f"There will be {note_ten} notes of Rs.10")

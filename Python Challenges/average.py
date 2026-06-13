c_1=int(input("Enter the speed of the first cyclist="))
c_2=int(input("Enter the speed of the second cyclist="))
c_3=int(input("Enter the speed of the third cyclist="))
avg=(c_1+c_2+c_3)/3
if avg>c_1 and avg>c_2:
    print("The average %d is higher than %d and %d" %(avg, c_1, c_2))
elif avg>c_2 and avg>c_3:
    print("The average %d is higher than %d and %d" %(avg, c_2, c_3))
elif avg>c_1 and avg>c_3:
    print("The average %d is higher than %d and %d" %(avg, c_1, c_3))
elif avg>c_1:
    print("The average %d is just greater than %d" %(avg, c_1))
elif avg>c_2:
    print("The average %d is just greater than %d" %(avg, c_2))
elif avg>c_3:
    print("The average %d is just greater than %d" %(avg, c_3))
else:
    print("The average %d is equal to %d, %d and %d" %(avg, c_1, c_2, c_3))


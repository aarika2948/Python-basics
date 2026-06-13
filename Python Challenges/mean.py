mean_og=38
total_no=40
wrong=36
correct=56
sum_og=(mean_og*total_no)
sum_new=(sum_og-(wrong-correct))
mean_new = sum_new/total_no
print(f"The corrected mean is {mean_new}")
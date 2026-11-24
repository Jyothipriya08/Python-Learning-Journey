# subject_1=int(input("Marks of the Telugu: "))
# subject_2=int(input("Marks of the Hindi: "))
# subject_3=int(input("Marks of the English: "))
# subject_4=int(input("Marks of the Maths: "))
# subject_5=int(input("Marks of the Science: "))
# Total_marks=subject_1+subject_2+subject_3+subject_4+subject_5
# Average_marks=Total_marks/5
# print("The total marks of all subjects is:",Total_marks)
# print("The Average marks of all five subjects is:",Average_marks)

# age_1=int(input("Enter the age1: "))
# age_2=int(input("Enter the age2: "))
# print(age_1>age_2)
# print(age_1<age_2)
# print(age_1!=age_2)
# print(age_1==age_2)
# print(age_1>=age_2)
# print(age_1<=age_2)

for num in range(10, 14):
    for i in range(2, num):
        if num%i==1:
            print(num)
            break

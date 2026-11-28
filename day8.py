#practise of for loop and while loop

# for i in range(1, 11):
#     print(i)

# for i in range(51):
#     if i%5==0:
#         print(i)

# for i in range(5):
#     print("Python")

# for i in range(2, 11, 2):
#     print(i)

# for i in range(1, 20):
#     if i%2!=0:
#         print(i)

# for i in range(1, 11):
#     print("7 x", i , "=", 7*i)

# total = 0
# for i in range(1, 11):
#     total = total + i
# print(total)

# count = 0
# for i in range(2, 21):
#     if i % 2 ==0:
#         count = count + 1
# print(count)

# for i in range(4, 50):
#     if i % 4 == 0:
#         print(i)

# for i in range(1, 21):
#     if i>10:
#         print(i)

# for i in range(1, 11):
#     print("4 x", i, "=", 4*i)

# total = 0
# for i in range(1, 21):
#     total = total + i
# print(total)



# sum = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)


# count = 0
# for i in range(1, 31):
#     if i%3==0:
#         count = count + 1
#         print(i)
# print("The count divisible by three are :",count)

count = 0
for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        count = count+1
print(count)
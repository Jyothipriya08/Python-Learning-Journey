#While loop

# i=1
# while i<=10:
#     print(i)
#     i=i+1

# i=100
# while i>=100 and i<=200:
#      if i%2==0:
#          print(i)
#          i=i+2
#      else:
#          print("not done")


# n=int(input("Enter a number: "))
# i=1
# sum=0
# while i<=n:
#     print(i)
#     sum=sum+i
#     i=i+1
# print(sum)


# n=int(input())
# i=1
# sum=0
# while i<=n:
#      if i%2==0:
#          print(i)
#          sum=sum+i
#      i=i+1
# print(sum)

# Reverse order of numbers 10 to 1
# i=10
# while(i>=1):
#     print(i)
#     i=i-1

#Multiples of 5 from 1 to 100 using while loop

# i=5
# while i<=100:
#     print(i)
#     i=i+5

# i=3
# while i<=30:
#     print(i)
#     i=i+3

# i=1
# sum=0
# while i<=50:
#     print(i)
#     sum=sum+i
#     i=i+1
# print(sum)

#1. print numbers from 1 to 10
# i=1
# while i<=10:
#     print(i)
#     i=i+1

#2.print numbers from 20 to 1 (reverse order)
# i=20
# while i>=1:
#     print(i)
#     i=i-1

#3.print all the even numbers from 1 to 50
# i=1
# while i<=50:
#     if i%2==0:
#         print(i)
#     i=i+1

#4.print all the odd numbers from 1 to 50
# i=1
# while i<=50:
#     if i%2!=0:
#         print(i)
#     i=i+1

#5. print all the multiples of 5 from 1 to 100
# i=5
# while i<=100:
#       print(i)
#       i=i+5

#6. Calculate the sum of numbers from 1 to 10
# i=1
# sum = 0
# while i<=10:
#     print(i)
#     sum=sum+i
#     i=i+1
# print(sum)

#7.calculate the sum off even numbers from 1 to 50
# i=1
# sum=0
# while i<=50:
#     if i%2==0:
#         print(i)
#         sum = sum+i
#     i=i+1
# print(sum)

#8.calculate the sum of odd numbers 1 to 50
# i=1
# sum=0
# while i<=50:
#     if i%2!=0:
#         print(i)
#         sum=sum+i
#     i=i+1
# print(sum)

# #9.print the table 5
# i = 1

# while i <= 10:
#     print("5 x", i, "=", 5 * i)
#     i = i + 1

#factorial of given number


n = int(input("Enter a number: "))
fact = 1

while n >= 1:
    fact = fact * n
    n = n - 1

print("Factorial =", fact)

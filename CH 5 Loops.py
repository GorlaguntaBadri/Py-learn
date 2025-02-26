# while lops example code .

"""count = 1
while count<=5 :
    print("hai Amar")
    count += 1"""
# first question and second question coding  .
# question print 1 - 100 and 100 to 1
#1. answer

"""i = 1
while i<=100 :
    print(i)
    i += 1
print("1 - 100 are printed")  """

# 1 . question code is correct .
# 2.
"""i = 100
while i>= 1 :
    print(i)
    i -= 1
print("100 - 1 printed ") """
#3rd question print any table  .
"""n = int(input("enter the table value  : "))
i = 1
while i<=10 :
    print(n*i)
    i += 1 """
#4th question is to print the square of the numbers
"""
n = int(input("enter the square value   : "))
i = 1
while i<=10 :
    print(i**n)
    i += 1"""
# for 4th question akka answer is
#num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""i = 0
while i < len(num):
    print(num[i])
    i += 1"""

#5th question
#num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]search a number x from this tuple using loop

"""num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("number to find : "))
i = 0
while i < len(num):
    if (num[i] == x):
        print("number found in list :", i)
    i += 1
else :
    print("not found ")"""
# now we are doing abt break and countinue keywords in the while loops
#break question example code
"""num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("number to find : "))
i = 0
while i < len(num):
    if (num[i] == x):
        print("number found in list :", i)
        break
    else:
        print("not found  ")
    i += 1"""
# continue keyword example code

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1


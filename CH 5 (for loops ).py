# basic code in for loop in tuple place  we can use list , str.. etc
"""tup = (1 , 2, 3 , 5, 6)
for num  in tup :
    print(num)"""
"""num = [1 , 2 , 3 ,4 ,5 ]
for val in num :
    print(val) """
"""str = "amar-nath"
for char in str :
    print(char) """
"""
str = "amar269"
for char in str :
    print(char)
else :
    print("str has end") """

# practice questions
# 1st question given a list and print those elements
"""num = [1, 4 , 9 , 16 , 25 , 36 ,49 , 64 , 81 ,100]
for val in num:
    print(val)
"""
# 2nd question use same list as tuple and serach for a number is found in that tuple or not
"""tup = (1, 3 ,4 ,9 ,5, 6 , 7 , 3)
x = int(input("enter the value : "))
i = 0
for el in tup :
    if (el == x):
        print("number found : " , i)
    i+=1"""
# using range() keyword in for loops there 3 types in range
"""for i in range(10):
    print(i)
# 2nd type
for k in range(2,10):
    print(k)
#3rd type
for z in range(2,10,2):
    print(z)
"""
# practice question on
"""for i in range(1,101,1):
    print(i)"""
# 2nd question pratice
"""for i in range(100 ,0 ,-1):
    print(i)"""
# 3rd question is to take user input and write table
"""n = int(input("enter the value : "))
for i in range(1,11):
    print(n*i)"""
# pass() keyword using in the for loops
"""for el in range(5):
    pass
print("pass keyword is working ") """

# practice questions
# 1st question take user input n number and sum them print and using "while loops"
"""n = int(input("enter the value : "))
sum = 0
for i in range (1 , n+1):
   sum += i
print("total sum = " , sum)"""
n = int(input("enter the value : "))
fact  = 1
for i in range (1 , n+1):
   fact  *=i

print("total sum = " , fact)



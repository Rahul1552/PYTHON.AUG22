#################################################
#  29.08.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 FLOW CONTROL IN PYTHON AND OPERATORS
#  https://docs.python.org/3/library/index.html
#################################################

# COMPARISON


'''
Python supports the usual comparison conditions from mathematics:
Equals:                     a == b #

Not Equals:                 a != b
Less than:                  a < b
Less than or equal to:      a <= b
Greater than:               a > b
Greater than or equal to:   a >= b
'''

# Logical operators
#  AND , OR ,NOT 
# Identity operators
#  IS , NOT IS 
# Membership operators
# IN , NOT IN 

###########################################
# If statements 
###########################################
#syntax

'''
if <condition>:
    block of code 
'''

# score = 100 # assigning the value to a variable 

# eg.1 to understand the syntax
# if score == 100:
#     print("You have scored a Century")


###########################################
# If... else statements 
###########################################
#syntax

'''
if <condition>:
    block of code
else:
    run this code
'''


# eg.2 using if..else block
# TAKING INPUT FROM USER

# marks  = int(input('Enter your marks : ')) # converting the i/p into integer
# print("Your marks are : ", marks)
# print(type(marks))

# if marks >= 35:
#     print("You have Passed the exam")
# else:
#     print("You have Failed  the exam")

# eg.3
p = int(input("Enter the Marks of P :"))
print("Your P marks are : " ,p)
c = int(input("Enter the Marks of C :"))
print("Your C marks are : " ,c)
m = int(input("Enter the Marks of M :"))
print("Your M marks are : " ,m)

avg = (p+c+m)/3
print("Your avg marks are : " ,avg)

if avg >= 35:
    print("You have passed")
else:
    print("You have failed")



###########################################
# print() 
###########################################

print('hello World') 
print('hello World', 'Shiva',)
print(34)
print(34+10)
print('34+10')

ans  = 99 +99

print(ans)
print('Your ans is :' ,99+99 )








    








#################################################
# 19.08.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 VARIABLES IN PYTHON 
# https://www.python.org/about/
#################################################


# Allowed variable names in Python 
'''
iam

i_am
__iam
_i_am
I_AM
I_AM
i_am_no1
_i_am_no1

__len__ # dunder len = double underscore length method , not to be used to name our varible


# below are not allowed to be used as a variable name in Python

1_am_
@_cool_boy
#1#23_
**123**_


'''

# overwrting a variable with different values

i_am = 1
print(i_am)

i_am = 100
print(i_am)

i_am = 1000
print(i_am)

print(i_am)

# one value to multiple variables 

i_am = "Indian"
we_are  = "indian"

print(i_am)
print(we_are)

i_am = we_are = "indian"

print(i_am)
print(we_are)

# box1 i_am Indian
# box2 we_are  Indian

# using id() to get  the memory address of the variable 
 
print(id(i_am))
print(id(we_are))


# many value to multiple variables 

i_am , we_are , they_are = "Person1" , "Person2" , "Person3"

print(i_am)
print(we_are)
print(they_are)
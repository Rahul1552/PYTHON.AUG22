
#################################################
# 24.08.2022 
#################################################
# TOPICS TO BE COVERED 
# VARIABLES IN PYTHON 
# INTRO BUILT-IN DATA TYPE OF PYTHON:
# https://www.python.org/
# https://www.programiz.com/python-programming/online-compiler/
#################################################


# ALLOWED VARIABLE NAMES IN PYTHON
'''
iam
i_am
_iam
_i_am
I_AM
_I_AM
I_AM_NO1
_i_am_no21
'''
# not allowed
'''
@cool_boy
1_23_nine
:rahul:59
'''
# not recommended , prohibited
# reserved in python , either in current use or reserved for future use
# these are DUNDER VARIABLES

'''
__class__
__init__
__save__
__rahul__

'''
iam = 1
print(iam)

iam = 100
print(iam)

# value can be allocated dynamically at any line of code


iam = "MinSkole"
print(iam)


# there in no liit in reassigning the value to a variable 


#  Assigning commonn value to multiple variables > Indian

iam = "Indian"
we_are = "Indian"
they_are  = "Indian"


print(iam)
print(we_are)
print(they_are)

print("***************")
iam = we_are =they_are = "Indian"
print(iam)
print(we_are)
print(they_are)


print("***************")

akash , amit ,mukesh = "roll1" , "roll2" ,"roll3"

print(akash)
print(amit)
print(mukesh)


print("***************")
iam = we_are =they_are = "Indian"
we_are = "North_Indian" # the memory addr will change
print(id(iam))
print(id(we_are))
print(id(they_are))


#################################################
# 26.08.2022
#################################################
# TOPICS TO BE COVERED 
# INTRO BUILT-IN DATA TYPE OF PYTHON:
# https://www.python.org/
# https://www.programiz.com/python-programming/online-compiler/
# https://docs.python.org/3/library/stdtypes.html#built-in-types
#################################################

# not recommended , prohibited
# reserved in python , either in current use or reserved for future use
# these are DUNDER VARIABLES

# __RAHUL__ = 100

# __init__ =100

# __main__ = "ramesh"



#################################################
# INTRO BUILT-IN DATA TYPE OF PYTHON:
#################################################


print("**********NUMERIC*******************")
# using type() to find the data-type
iam = -1
print(type(iam))

iam = -1.1
print(type(iam))

iam = -1+4j
print(type(iam))


iam = -1.0
print(type(iam))


print("**********STRINGS*******************")

iam = 'r'
print(type(iam))

iam = 'rahul'
print(type(iam))


iam = 'rahul likes Python3.0'
print(type(iam))


iam = 'வணக்கம்'
print(type(iam))



iam = "-1+4j"
print(type(iam))

print("**********STRINGS HAVING ESCAPE CHAR*******************")

iam = r"C:\Users\RAHUL\Documents\OnePython\3.August_22\CLASS"
print(type(iam))

iam = "C:\\Users\RAHUL\Documents\OnePython\\3.August_22\CLASS"
print(type(iam))



print("**********LIST*******************")

i_am_list = [2,4,6,8,10]
print(i_am_list)
print(type(i_am_list))

i_am_list = [2.0,4.0,6,8,10,"Rahul","chetan","mukesh"]
print(i_am_list)
print(type(i_am_list))

i_am_list = ["This is  a sentence " ,"inside a list" , 22]
print(i_am_list)
print(type(i_am_list))

 
print("**********TUPLES*******************")


shiva = (2,4,6,8,10)
print(shiva)
print("Type of shiva is :" ,type(shiva))


print("**********DICTIONARY*******************")

dict1 = {
    # key(has to be unique) : value
    "r" : "Rahul",
    "s" : "Shivaprasad",
    "g" : "Ganesh",
    "s" : "Sankarshan",
    "r1" : "Rahul"

}

print(dict1)
print(type(dict1))


dict_even = {
    # key(has to be unique) : value
    2 : 22,
    4 :44 ,
    6 : 66
}
print(dict_even)
print(type(dict_even))


# HW 

am_i_string = ''
print(type(am_i_string ))
am_i_string = ""
am_i_list = []
am_i_tuple = ()
am_i_dict = {}


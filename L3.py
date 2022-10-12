
#################################################
# 23.08.2022 
#################################################
# TOPICS TO BE COVERED 
# INPUT FUNCTION 
# ESCAPE SEQUENCE
# https://www.python.org/
# https://www.programiz.com/python-programming/online-compiler/
#################################################


# print(" Hello World ")
# print(" Good Evening Chinmay ")



# # name1  =  input("Please Enter Your name : ")
# # print(" Good Evening : " ,name1)


# lucky_num = input("Enter you Lucky Number : ") # it will be considered as  a string
# lucky_num = int(input("Enter you Lucky Number : ")) # it will be considered as  a string
# print(lucky_num)

# #type casting = moulding
# print(int(lucky_num) + 5 )


#################################################
# ESCAPE SEQUENCE
#################################################

students  = " The students are Nilesh   Monica  Ashok"
print(students)

students  = " The students are \tNilesh \tMonica \tAshok"
print(students)


fav_students  = "My fav students are \nrollno.1 , \nrollno.4 , \nrollno.7 "
print(fav_students)

my_address = '''
Shri xyz ,
Flat no 1101/b 23/9
bandra east
mumbai
400065
'''
print(my_address)
my_address = "Shri xyz ,\nFlat no 1101/b 23/9 \nbandra east \nmumbai \n400065"


print(my_address)



#use of single
print('i am happy today')
#use of double
print("i'm happy today") # recommended
#use of triple 
print('''suresh said , "he is happy today"''')

# for multi line sentences

status  =  '''
suresh said ,
"he is happy today"
'''

# comments are for humans | coder , not to be interpreted by Python

# multiline comments using ''' '''
'''
this is for the next coder for 
reviewing the code
before delivery in 
production
'''



students  = " The students are \tnilesh \tmonica \tashok \ttanmay"
print(students)


print("C:\\Users\RAHUL\Documents\OnePython\\3.August_22\CLASS")
print(r"C:\Users\RAHUL\Documents\OnePython\3.August_22\CLASS")
print(R"C:\Users\RAHUL\Documents\OnePython\3.August_22\CLASS")


# Escape Character Meaning
# \”                Double quote
# \’                Single quote
# \\                backslash
# \n                New line
# \r                Carriage Return
# \t                Horizontal tab
# \b                Backspace
# \f                form feed
# \v                vertical tab
# \0                Null character
# \N{name}          Unicode Character Database named Lookup
# \uxxxxxxxx        Unicode Character with 16-bit hex value XXXX
# \Uxxxxxxxx        Unicode Character with 32-bit hex value XXXXXXXX
# \ooo              Character with octal value OOO
# \xhh              Character with hex value HH

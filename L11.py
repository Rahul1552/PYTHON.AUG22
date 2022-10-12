#################################################
#  02.09.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 FLOW CONTROL IN PYTHON AND OPERATORS
#################################################

# voter_age = int(input("Please enter your age : "))

# if 18 <= voter_age <=64:
#     print("You are eligible to vote !!!")
#     print("Use your Voting power properly")

# elif 65 < voter_age <=100: 
#     print("You are eligible to vote !!!")
#     print("You can ask the staff for help !!!")

# else:
#     print("You not are eligible to vote !!!")
#     print("Please wait for {} years".format(18- voter_age))


x = int(input('Enter Pin code :'))

if x == 100:
    print("Welcome to city A")

elif x == 200:
    print("Welcome to city B")

elif x == 300:
    print("Welcome to city C")

elif x == 400:
    print("Welcome to city D")

elif x == 500:
    print("Welcome to city E")

else:
    print("Enter correct value")
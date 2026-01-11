
# checking the strength of a password entered by the user

password = input ("enter your password: ")


# using if else loop// this will only run the loop once and give the output


if len(password)>= 8: #len() is a python built in function to count the items
    print("password length is fine")
else:
    print("password must be 8 chanracter long")



# using the while loop // this will ask to re-enter the password until meets the loop requirement.

while len(password)< 8:
    print("password must be 8 character long")
    password = input ("re-enter your password: ")

print("password length is valid")





# checking if the password has any upper case or not 
# checking if the password has any special character 
# checking if the password includes common passwords 

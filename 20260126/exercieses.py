# store_number = input("Enter a number to store: ")

# store_number = int(store_number)

# if store_number > 10:
#     print("The number is stored")
#     print("Number is greater than 10")
# else:
#     print("Try increasing the number to get it stored.")

# check_number = input("Enter a number to check E/O: ")

# # if int(check_number) % 2 == 0:
# #     print("Even Number")
# # else:
# #     print("Odd Number")

# if int(check_number) % 2 != 0:
#     print("Odd Number")
# else:
#     print("Even Number")


# c_number = input("Enter number to check if that is divisible by 3 / 5 or both: ")

# i_number = int(c_number)


# if i_number % 3 == 0 and i_number % 5 == 0:
#     print(f"The {i_number} is divisible by both")
# elif i_number % 5 == 0: 
#     print(f"The {i_number} is divisible by 5")
# elif i_number % 3 == 0:
#     print(f"The {i_number} is divisible by 3")
# else:
#     print("It is not divisible by any of these")

userName = input("Enter your username: ")
userPass = input("Enter your passcode: ")

databaseUserName = "Simran"
databaseUserPass = "NahiPata"

if userName == databaseUserName:
    print("Username verified... now checking password")
    
    if ( userPass == databaseUserPass ):
        print("Login Successful")
    else:
        print("Login Unsuccessful")
else:
    print("User not found!")



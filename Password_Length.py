
#########################################################
###       Function to get the password Length.      ###
# Acceptance Criteria:
# 1. Minimum should be 6 characters
# 2. Only numbers should be accepted as input
#########################################################

def password_length(num):
    if type(num) == int and num >= 6:
            in_tot_length = num
            # placeholder till the password generator function is defined, will be replaced by a return statement
            print(f'{num} is a Valid input')
            # the 'in_tot_length' will be used for generating the password
            # return in_tot_length
    else:
        print(f"{num} is an Invalid Input! Please input a number that is greater than or equal to 6")


password_length(2)
password_length(6)
password_length(20)
password_length('txt')

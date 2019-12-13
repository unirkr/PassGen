
############################################################################
### Function to get the no. of numbers the user want in password   ###
############################################################################

def num_of_characters(num):
    if type(num) == int and num >= 0:
        in_num_of_numbers = num         # in_characters variable is used to store the number of numbers/letters that the user wants in the password
        # placeholder till the password generator function is defined, will be replaced by a return statement
        print(f'{num} is a Valid input')
        # the 'in_characters' will be used for generating the password
        # return in_characters
    else:
        print(f"{num} ia an Invalid Input! Please input a valid number that is greater than or equal to 0")


num_of_characters(-1)
num_of_characters(0)
num_of_characters(100)
num_of_characters('test')
############################################################################
###         Welcome to the PassGen wiki!        ###
# Write a program, which generates a random password for the user.
# Ask the user how long they want their password to be,
# and how many letters and numbers they want in their password.
# Have a mix of upper and lowercase letters,
# as well as numbers and symbols.
# The password should be a minimum of 6 characters long.
############################################################################

import random

def Password_Generator(in_tot_length, in_num_of_numbers, in_special_char):
    chars_numbers = '1234567890'
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars_with_special_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+<>?'

    password = ''
    new_password = ''
    new_length = ''

    for num in range(in_num_of_numbers):
        password += random.choice(chars_numbers)

    new_length = in_tot_length-len(password)

    if in_special_char == True:
        for i in range(new_length):
            password += random.choice(chars_with_special_char)
    else:
        for i in range(new_length):
            password += random.choice(chars)

    temp_password_list=list(password)
    random.shuffle(temp_password_list)

    new_password =''
    for char in temp_password_list:
       new_password += char

    print(f'Password is {new_password}')



Password_Generator(20,5,True)
Password_Generator(7,3,False)

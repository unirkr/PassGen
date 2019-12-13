
############################################################################
###       Function to add special characters as needed by user.      ###
# Acceptance Criteria:
# Special characters will be included in password if user requests for it
# Possible special characters ~!@#$%^&*()_+<>?
############################################################################

def special_character(boo):
    in_special_char = None
    if boo == True:
        in_special_char = boo
        # placeholder till the password generator function is defined, will be replaced by a return statement
        print(f'{boo} is a Valid input')
        # the 'in_special_char' will be used for generating the password
        # return in_special_char
    else:
        print(f'{boo} is an Invalid input')

special_character(True)
special_character(False)
special_character('Yes')
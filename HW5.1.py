# ДЗ 5.1. Ім'я змінної

import string; import keyword


user_variable = input("Enter the variable's name: ")
# user_variable =  "___" 
# user_variable =  "get value" 
# user_variable =  "get!value" 
# user_variable =  "get_Value" 
# user_variable =  "some_super_puper_value"
# user_variable =  "assert_exception"

# check if starts with digit
starts_with_digit = True if user_variable[0] in string.digits else False

# check if has space
has_space = True if " " in user_variable else False

# check if is keyword
is_keyword = True if user_variable in keyword.kwlist else False

# check if has double underline ("__")
has_duoble_underline = True if "__" in user_variable else False

# check if has punctuation except of "_"
for i in string.punctuation:
    if i == "_":
        continue

    has_punctuation = user_variable.find(i)

    if has_punctuation == -1:
        has_punctuation = False
    else:
        has_punctuation = True
        break

# check if has capital
for i in string.ascii_uppercase:
    if i in user_variable:
        has_capital = True
        break
    else:
        has_capital = False

# main check
if starts_with_digit or has_space or is_keyword or has_punctuation or has_duoble_underline or has_capital:
    print(False)
else:
    print(True)

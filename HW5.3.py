# ДЗ 5.3. hashtag

import string

# my_string = input("Enter your string: ")
# my_string = "s a<<<<< a JJJJJJJJJ  f                                                        ao    s s                                            ()()()()()($%#@$%^&*() m)"
my_string = "s" * 138 + "mmmmm"
# my_string = "i like python community!"
# my_string = "Should, I. subscribe? Yes!"

# print(my_string, len(my_string), sep="\n")

lst_my_string = list(my_string)

for _ in range(len(lst_my_string)):
    for i in lst_my_string:
        if i in string.punctuation:
            lst_my_string.remove(i)

join_lst = "".join(lst_my_string)
make_title = join_lst.title()
split_string = make_title.split()
split_string.insert(0, "#")
final_result = "".join(split_string)

print(final_result[:140])

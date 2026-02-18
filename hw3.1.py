# ДЗ 3.1. Найпростіший калькулятор

# num1, num2 = int(input("Ведіть перше число: ")), int(input("Введіть друге число: "))
# sign = input("Введіть арефметичний знак: ")

# if sign == "+":
#     print(f'{num1} + {num2} = {num1 + num2}')

# if sign == "-":
#     print(f'{num1} - {num2} = {num1 - num2}')

# if sign == "*":
#     print(f'{num1} * {num2} = {num1 * num2}')

# if sign == "/":
#     if num2 == 0:
#         print("На нуль ділити не можна !!!")
#         num2 = int(input("Змініть значення для другого числа: "))
#         if num2 == 0:
#             print('Почни з початку')
#         else:
#             print(f'{num1} / {num2} = {num1 / num2}')
        
#     else:
#         print(f'{num1} / {num2} = {num1 / num2}')



# ДЗ 3.2. Перемістити елемент у списку

lst = [10, 43, 25, 14.8, 90]
lst_1 = [1]
lst_empty = []

print(lst)
print(lst_1)
print(lst_empty)

print('***' * 20)

x = lst.pop(-1)
lst.insert(0, x)
print(lst)

y = lst_1.pop(-1)
lst_1.insert(0, y)
print(lst_1)

if bool(lst_empty) == False:
    print(lst_empty)
else:
    z = lst_empty.pop(-1)
    lst_empty.insert(0, z)
    print(lst_empty)

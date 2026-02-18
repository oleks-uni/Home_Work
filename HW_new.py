# tasks for STR

# Напишіть функцію, яка приймає рядок і повертає його довжину.
def find_len(some_str: str) -> int:

    if type(some_str) is str:
        return len(some_str)
    else:
        return f"Error: the type of '{some_str}' is not str"

# print(find_len("test"))


# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.
def concat(str_1: str, str_2: str) -> str:

    if all([type(str_1) is str, type(str_2) is str]):
        return str_1 + str_2
    else:
        return f"Error: invalid type"

# print(concat("123", "321"))



# tasks for INT/FLOAT

# Реалізуйте функцію, яка приймає число і повертає його квадрат.
def square(number: int) -> int:

    if type(number) is int:
        return number ** 2
    else:
        return f"Error: the type of '{number}' is not str"
    
# print(square(3))


# Створіть функцію, яка приймає два числа і повертає їхню суму.
def suma(num_1: int, num_2: int) -> int:

    if all([type(num_1) is int, type(num_2) is int]):
        return num_1 + num_2
    else:
        return f"Error: invalid type"
    
# print(suma(2, 5))


# Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.
def div(num_1: int, num_2: int) -> [float,  int]:

    if all([type(num_1) is int, type(num_2) is int]):

        if num_2 == 0:
            return f"You can not divide by '0'!"
        else:
            whole = num_1 // num_2
            remainder = num_1 % num_2

            return whole, remainder
        
    else:
        return f"Error: invalid type"
    
# print(div(10, 3))
# print(div(10, 0))



# tasks for LIST

# Напишіть функцію для обчислення середнього значення списку чисел.
def averege(lst: list) -> int:
    
    lenght_lst = len(lst)

    sum = 0

    for i in lst:
        sum += i

    return f"The average number is '{sum // lenght_lst}'" 

# print(averege([5, 5, 5, 5, 5]))


# Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.
def list_ext(lst_1: list, lst_2: list) -> list:

    lst_1.extend(lst_2)

    return lst_1

# print(list_ext([1, 2, 3, "5"], ['str', "pop"]))



# tasks for DICT

# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
def dict_value(dct: dict) -> list:

    return dct.values()

car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(dict_value(car_dict))


# Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.
def dict_upd(dct_1: dict, dct_2:dict) -> dict:

    dct_1.update(dct_2)
    
    return dct_1

# print(dict_upd(car_dict, {"color": "red", "status": "new"}))



# tasks for SET

# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.
def set_upd(set_1: set, set_2: set) -> set:

    set_1.update(set_2)

    return set_1

set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft"}
result_set = set_upd(set_1, set_2)

# print(result_set)


# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.
def set_sub(set_1: set, set_2: set) -> bool:

    return set_1.issubset(set_2)

# print(set_sub(set_2, result_set))
# print(set_sub(result_set, set_2))



# tasks for CONDITIONS/LOOPS

# Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
def is_even(number: int) -> str:

    if number % 2 == 0:
        return "Парне"
    else:
        return "Непарне"
    
# print(is_even(5))
# print(is_even(10))


# Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
def find_even(lst: list) -> list:

    new_lst = []

    for i in lst:
        if i % 2 == 0:
            new_lst.append(i)
    
    return new_lst

# print(find_even([1, 6, 2, 4, 7, 23, 90]))

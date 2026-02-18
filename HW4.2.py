# ДЗ 4.2. Знайти суму елементів із парними індексами

lst = [0, 1, 7, 2, 4, 8]
# lst = [1, 3, 5]
# lst = [6]
# lst = []

x = 0

if lst:
    for i in lst[::2]:
        x += i

    print(x * lst[-1])
else:
    print(x)

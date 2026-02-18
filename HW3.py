num1, num2 = int(input("Ведіть перше число: ")), int(input("Введіть друге число: "))
sign = input("Введіть арефметичний знак: ")

match sign:
    case "+":
        print(f'{num1} + {num2} = {num1 + num2}')
    case "-":
        print(f'{num1} - {num2} = {num1 - num2}')
    case "*":
        print(f'{num1} * {num2} = {num1 * num2}')
    case "/":
        if num2 == 0:
            print("На нуль ділити не можна!")
            num2 = int(input("Введіть інше значення для другого числа: "))
            if num2 == 0:
                print("Спробуй з початку")
            else:
                print(f'{num1} / {num2} = {num1 / num2}')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')

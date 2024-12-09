number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
if number1 == number2 and number2 == number3:
    print('3')
elif number1 == number2 or number1 == number3 or number2 == number3:
    print('2')
else:
    print('0')
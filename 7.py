simb = input('Введите число abc: ')
if simb.isdigit() and len(str(simb)) == 3:
    print(f'Введено целое число: {simb}')
else:
    while not simb.isdigit():
        simb = input('Ошибка, попробуйте еще раз. Введите число abc: ')
        if simb.isdigit() and len(str(simb)) == 3:
            print(f'Введено целое число: {simb}')

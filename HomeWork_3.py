# Задача 1
print('Задача 1 \n')
num_1 = float(input('Введите первое число = '))
num_2 = float(input('Введите второе число = '))
op = str(input('Введите операнд над числами  = '))
if op == chr(43) :
    print(num_1 + num_2)
elif op == chr(45):
    print(num_1 - num_2)
elif op == chr(42):
    print(num_1 * num_2)
elif op == chr(47):
    print(num_1 / num_2)
elif op == chr(94):
    print(num_1 ** num_2) # num_1 - число которое нужно возвести в степень;num_2- степень в которую нужно возвести число
else :
    print("Вы ввели не правильные значения\n")
# Задача 2
print('Задача 2 \n')

n = int(input('Введите натуральное число N = '))
for i in range(n):
    if i**2 <= n :
        print(i ** 2 , end=' ')
else:
    print('  \n')
# Задача 3
print('Задача 3 \n')

num = int(input('Введите число = '))
if num > 1:
    for i in range(2 , num):
        if num % i == 0 :
            print(f'{num} - сложное число  ')
            break
    else:
        print(f'{num} - простое число ')
else:
    print('Вы ввели не то число \n')

print('Задача 4 \n')
m = int(input('Введите количество грибов =  '))
m1 = " грибов "
m2 = " гриба "
m3 = " гриб "
if m >= 0 :
    if m == 0 :
        print(f'Маша нашла в лесу {m} ' + str(m1))
    elif m % 100 >=10  and m % 100 <= 20:
        print(f'Маша нашла в лесу {m} ' + str(m1))
    elif m % 10 == 1 :
        print(f'Маша нашла в лесу {m} ' + str(m3))
    elif m % 10 >= 2  and m % 10 <= 4:
        print(f'Маша нашла в лесу {m} ' + str(m2))
    elif m % 10 >= 5  and m % 10 <= 9:
        print(f'Маша нашла в лесу {m} ' + str(m1))
else:
    print()
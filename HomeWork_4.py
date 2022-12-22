print("Задание 1 \n")
my_string = '0123456789'
my_string = str(my_string)
for i in my_string:
        for j in my_string:
            result = int (i+j)
            print(result)




print("Задание 2 \n")
print('A\n')
h = int(input('Введите высоту = '))
for string in range(1, h + 1 ):
    for space in range( 0 , h*2 -string*2):
        print(' ', end = '')
    for star in range(string + (string - 1)):
        print('*' , end=' ')
    print()
print('B\n')
h = int(input('Введите высоту = '))
for string in range(1, h + 1 ):
    for space in range( 0 , h*2 -string*2):
        print(' ', end = '')
    for star in range(string + (string - 1)):
        if star == 0 or star == string + (string - 1 ) - 1 or string == h:
            print('*', end = ' ')
        else:
            print(' ', end= ' ')
    print()
print('C\n')
h = int(input('Введите высоту = '))
for string in range(1, h + 1 ):
    for space in range( 0 , h*2 -string*2):
        print(' ', end = '')
    for star in range(string + (string - 1)):
        print('*' , end=' ')
    print()
for string in range(1, h):
    for space in range(0, string * 2):
        print(' ', end='')
    for star in range(h * 2 - ((string + 1) + string)):
        if star == 0 or star == h*2 - ((string+1) + (string + 1)) or string == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('D\n')
h = int(input('Введите высоту = '))
for string in range(1, h + 1 ):
    for space in range( 0 , h*2 -string*2):
        print(' ', end = '')
    for star in range(string + (string - 1)):
        print('*' , end=' ')
    print()
for string in range(1, h):
    for space in range(0, string * 2):
        print(' ', end='')
    for star in range(h * 2 - ((string + 1) + string)):
        if star == 0 or star == h*2 - ((string+1) + (string + 1)) or string == h or star == h - (string +1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()










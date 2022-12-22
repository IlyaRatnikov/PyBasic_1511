h = int(input('Введите высоту = '))
for string in range(1, h):
    for space in range(0, string * 2):
        print('-', end='')
    for star in range(h * 2 - ((string + 1) + string)):
        if star == 0 or star == h*2 - ((string+1) + (string + 1)) or string == h or star == h - (string +1):
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()
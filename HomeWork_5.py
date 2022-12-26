from random import randint
print('Задание 1 \n')
my_list = [randint(1 , 500) for i in range(300) ]
for j in my_list:
    if j > 100:
        print(j , end=' ')
print()
print()


print('Задание 2 \n')

my_list = [randint(1 , 500) for i in range(300) ]
my_results = []   # а можно было б написать my_results = my_list ?
for j in my_list:
    if j > 100:
        my_results.append(j)
print(my_results)
print()

print('Задание 3 \n')

my_list = [randint (8, 487) for i in range(randint(1,4))]
print(my_list)
if len(my_list) < 2 :
    my_list.append(0)
    print(my_list)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)
print()

print('Задание 6 \n')

li1 = [randint(5 , 15) for i in range(10) ]
print(li1)
li3 =[]
for n in li1:
    if n not in li3:
        li3.append(n)
print(li3)
li2 = [randint(1 , 10) for i in range(10) ]
print(li2)
li4 = []
for m in li2:
    if m not in li4:
        li4.append(m)
print(li4)
print(len(li3)+len(li4))









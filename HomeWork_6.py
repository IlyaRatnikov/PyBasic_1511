from random import randint

print('Задание 3 \n')
my_list_1 = [i for i in range(10)]
my_list_2 = [i for i in range(15)]
my_result = []
for i in my_list_1[::2]:
        my_result.append(i)
for n in my_list_2[1::2]:
       my_result.append(n)
print(my_result)
print()

print('Задание 11 \n')

my_str = set('aaassssddffgghhjkll')
print(my_str)
print()


print('Задание 4 \n')

my_list = [randint(1,5) for i in range(4)]
print(my_list)
new_list = []
for i in my_list:
    new_list.append(i)
new_list.append(new_list.pop(0))
print(new_list)
print()

print('Задание 5 \n')

my_list1 = [randint(1,5) for i in range(4)]
print(my_list1)
my_list1.append(my_list1.pop(0))
print(my_list1)
print()

print('Задание 6 \n')

my_str1='43 больше чем 34 , но меньше чем 56'
list_sum=[]
for i in my_str1.split():
    if i.isdigit() == True:
        i = int(i)
        list_sum.append(i)
list_sum = sum(list_sum)
print(list_sum)
print()

print('Задание 10 \n')

my_list = [1, 2,'gffgdg', 3, "11", "22", 33]
my_list2 = []
for i in my_list:
    if i == str(i):
        my_list2.append(i)
print(my_list2)
print()

print('Задание 12 \n')

my_str1 ='gdgh2345322ighifjjweisfihgiu'
my_str2 ='wjffh4234215seuif'
my_set1 = set(my_str1)
my_set2 = set(my_str2)
my_set3 = my_set1 | my_set2
my_list = list(my_set3)
print(my_list)





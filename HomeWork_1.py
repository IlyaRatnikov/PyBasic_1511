#Даны две строки.
# Создать список в который поместить те символы,которые есть в обеих строках хотя бы раз.

my_str1 ='gdgh2345322ighifjjweisfihgiu'
my_str2 ='wjffh4234215seuif'
my_set1 = set(my_str1)
my_set2 = set(my_str2)
my_set3 = my_set1 | my_set2
my_list = list(my_set3)
print(my_list)



my_list = input().split()
print(my_list)
a = 1
for i in my_list:
    if a % 2 != 0:
        my_list.insert(a + 1, i)
        del my_list[a - 1]
    a += 1
print(my_list)

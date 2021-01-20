my_list = [7, 5, 3, 3, 2]
b = 0
a = int(input())
if a <= my_list[-1]:
    my_list.append(a)
else:
    for i in my_list:
        if a > i:
            my_list.insert(b, a)
            break
        b += 1
print(my_list)
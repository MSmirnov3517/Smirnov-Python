def int_func(a):
    b = a.capitalize()
    return b


s = input().split()
for i in s:
    print(int_func(i), end=' ')
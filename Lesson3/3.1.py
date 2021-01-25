def my_func1(a, b):
    return a / b


a = int(input())
b = int(input())
if b == 0:
    print('На 0 делить нельзя!')
    b = int(input())
print(my_func1(a, b))

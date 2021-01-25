def my_func(a, b):
    i = 1
    c = a
    while i < abs(b):
        c = c * a
        i += 1
    return c


print(my_func(999.50, -5))

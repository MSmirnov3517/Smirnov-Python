sum = 0
stop = 0
while stop != 1:
    a = input().split()
    for i in a:
        if i == 'q':
            stop = 1
            break
        sum += int(i)
    print(sum)
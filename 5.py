def f(n):
    a = str(n)
    b = [(int(a[0]) + int(a[1])), (int(a[1]) + int(a[2]))]
    return str(sorted(b)[1]) + str(sorted(b)[0]) 

for i in range(100, 1000):
    r = f(i)
    if r == "1711":
        print(i)
        break

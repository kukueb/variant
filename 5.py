def f(n):
    b = bin(n)[2:]
    b = b + str(b.count("1")%2)
    b = b + str(b.count("1")%2)
    return int(b, 2)

for i in range(1, 100):
    r = f(i)
    if r > 55:
        print(r)
        break

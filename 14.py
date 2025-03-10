def f(n, m):
    b = ""
    while n > 0:
        b = str(n%m) + b
        n //= m
    return b

print(f(16**18 * 4**10 - 4**6 - 16, 4).count("3"))

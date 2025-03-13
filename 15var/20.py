def f(s, n):
    if s >= 100 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(s+1, n+1), f(s**2, n+1)])
    return any([f(s+1, n+1), f(s**2, n+1)])

for s in range(2, 100):
    if f(s, 0):
        print(s)

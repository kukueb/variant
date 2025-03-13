def f(s, n):
    if s >= 100 or n > 4:
        return n == 4 or n == 2
    if n % 2 == 0:
        return all([f(s+1, n+1), f(s**2, n+1)])
    return any([f(s+1, n+1), f(s**2, n+1)])

for s in range(2, 100):
    if f(s, 0):
        print(s)
        break

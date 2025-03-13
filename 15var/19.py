def f(s, n):
    if s >= 100 or n > 2:
        return n == 2
    if n % 2 == 0:
        return any([f(s+1, n+1), f(s**2, n+1)]) # any, так как ход Пети неудачный 
    return any([f(s+1, n+1), f(s**2, n+1)])

for s in range(2, 100):
    if f(s, 0):
        print(s)
        break

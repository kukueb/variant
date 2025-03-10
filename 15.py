p = [x for x in range(12, 62+1)]
q = [x for x in range(52, 92+1)]

mn = 10**6
for a0 in range(1, 1000):
    for a1 in range(a0):
        f = 1
        rng = range(a1, a0+1)
        for x in range(1000):
            exp = (not(not(x in rng) and (x in p)) or (x in q))
            if exp != 1:
                f = 0
                break
        if f == 1:
            mn = min(mn, len(rng))
print(mn)

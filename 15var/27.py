l = [int(x) for x in open("27-A.txt")]

k = 0
for i in range(len(l)-1):
    for j in range(i, len(l)):
        s = l[i] + l[j]
        ml = l[i] * l[j]
        if s % 4 == 0 and ml % 59049 == 0:
            k += 1

print(k)

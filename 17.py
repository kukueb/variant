l = [int(x) for x in open("17.txt").readlines()]

mn7 = 10**6
for i in l:
    if abs(i)%10 == 7:
        mn7 = min(mn7, i)


mx_s = 0
k = 0
for i in range(len(l)-1):
    if abs(l[i])%10 == abs(l[i+1])%10 and ((abs(l[i])%7 == 0) != (abs(l[i+1])%7 == 0)) and (l[i]**2 + l[i+1]**2) <= mn7**2:
        k += 1
        mx_s = max(mx_s, l[i]**2 + l[i+1]**2)

print(k, mx_s)

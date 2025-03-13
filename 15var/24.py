s = open("24_58328.txt").readline()

k = 0
mx = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        k += 1
    else:
        mx = max(k, mx)
        k = 0
    
print(mx+1)

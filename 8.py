a = "ABCDEF"
k = 0
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                for i5 in a:
                    s = i1+i2+i3+i4+i5
                    if i1 != "F" and i5 != "A":
                        k+=1

print(k)
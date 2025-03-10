l = open("Вариант/А тут ещё один/9.csv").readlines()

k = 0
for i in l:
    l1 = [int(a) for a in i.split(";")]
    l1 = sorted(l1)
    if l1[2] < l1[1] + l1[0]:
        k += 1

print(k)

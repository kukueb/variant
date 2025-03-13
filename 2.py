print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w <= y) and (not(y) == x) and (x or z)
                if f == 1:
                    print(x,y,z,w)
                    # 4 : 010 10 110 10 010 10 100

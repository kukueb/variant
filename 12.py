for a in range(1, 35):
    for b in range(1, 35):
        for c in range(1, 35):
            s = "0" + "1"*a + "2"*b + "3"*c + "0"
            while not "00" in s:
                s = s.replace("01", "210", 1)
                s = s.replace("02", "3101", 1)
                s = s.replace("03", "2012", 1)
            if s.count("1") == 70 and s.count("2") == 56 and s.count("3") == 23:
                print(a + b + c + 2)
                exit()

def m(n):
    return n + 1, n**2

def game(n):
    if any(x >= 100 for x in m(n)): return "win1"
    if all(game(y) == "win1" for y in m(n)): return "loss2"
    if any(game(z) == "loss2" for z in m(n)): return "win3"
    if all(game(x1) == "win3" for x1 in m(n)): return "loss4"

for s in range(2, 99):
    if game(s) == "win3":
        print(s)


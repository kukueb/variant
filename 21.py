def m(n):
    return n+1, n**2

def game(n):
    if any(x >= 100 for x in m(n)): return "win1"
    if all(game(n) == "win1" for n in m(n)): return "loss2"
    if any(game(n) == "loss2" for n in m(n)) : return "win3"
    if all()

for s in range(2, 99):


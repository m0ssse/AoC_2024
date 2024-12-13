def solve(data):
    res1 = 0
    res2 = 0
    extra = 10**13
    for dxa, dya, dxb, dyb, X, Y in data:
        cost1 = get_cost(dxa, dya, dxb, dyb, X, Y)
        if cost1:
            res1+=cost1
        cost2 = get_cost(dxa, dya, dxb, dyb, X+extra, Y+extra)
        if cost2:
            res2+=cost2
    print(res1)
    print(res2)

def get_cost(dxa, dya, dxb, dyb, X, Y):
    D = dxa*dyb-dxb*dya
    if D==0:
        return
    na_nominator = dyb*X-dxb*Y
    if na_nominator%D!=0:
        return
    nb_nominator = dxa*Y-dya*X
    if nb_nominator%D!=0:
        return
    return 3*na_nominator//D+nb_nominator//D
    


fname = "day13_input.txt"
with open(fname) as file:
    data = file.read().split("\n\n")
data = [part.split("\n") for part in data]
cranes = []
for button_a, button_b, prize in data:
    ax, ay = [int(s.split("+")[-1]) for s in button_a.split(": ")[-1].split(", ")]
    bx, by = [int(s.split("+")[-1]) for s in button_b.split(": ")[-1].split(", ")]
    px, py = [int(s.split("=")[-1]) for s in prize.split(": ")[-1].split(", ")]
    cranes.append((ax, ay, bx, by, px, py))

solve(cranes)

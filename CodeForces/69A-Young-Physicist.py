def equilibrium(n):
    x,y,z = [],[],[]
    for i in range(n):
        x.append(int(input()))
        y.append(int(input()))
        z.append(int(input()))
    if sum(x) == 0 and sum(y) == 0 and sum(z) == 0:
        return "YES"
    return "NO"
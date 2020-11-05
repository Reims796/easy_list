def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rshift_list(mass):
    a = ft_len(mass)
    x = []
    for i in range (a):
        x.append(mass[i-1])
    for i in range (a):
        mass[i] = x[i]
    return mass

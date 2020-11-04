def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rshift_list(mass):
    d = ft_len(mass)
    i = 1
    d -= 1
    x = []
    x.append(mass[d - 1])
    for i in range(d):
        x.append(mass[i])
        i += 1
    return x

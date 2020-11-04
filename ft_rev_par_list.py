def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rev_par_list(mass):
    i = 1
    x = []
    d = ft_len(mass)
    if d % 2 == 0:
        for i in range(d):
            x.append(mass[i])
            x.append(mass[i-1])
            i += 2
        return r
    else:
        d = d - 1
        for i in range(d):
            x.append(mass[i])
            x.append(mass[i-1])
            i += 2
        x.append(mass[d])
        return x
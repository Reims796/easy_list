def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_super_shift_list(mass, n):
    i = 0
    d = ft_len(mass)
    x = []
    z = d
    if n >= 0:
        for i in range(n):
            x.append(mass[d - 1])
            d -= 1
            i += 1
        i = 0
        for i in range(z - n):
            x.append(mass[i])
            i += 1
        return r
    else:
        i = n - n * 2
        for i in range(d):
            x.append(mass[i])
            i += 1

        i = 0
        while i > n:
            x.append(mass[i - i * 2])
            i += 1
        return x




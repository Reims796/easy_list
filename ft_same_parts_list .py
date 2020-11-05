def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_same_parts_list(mass):
    d = ft_len_mass(mass)
    x = 0
    i = 0
    for i in range(d):
        if mass[i] > mass[i - 1] and i > 0:
            x += 1
        i += 1

def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_even_parts_list(mass):
    i = 0
    x = []
    d = ft_len_mass(mass)
    for i in range(d):
        if mass[i] % 2 == 0:
            x.append(mass[i])
        i += 1
    return x

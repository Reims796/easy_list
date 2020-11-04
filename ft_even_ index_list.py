def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_even_index_list(mass):
    d = ft_len_mass(mass)
    i = 0
    x = []
    for i in range(d):
        if i % 2 == 0:
            x.append(mass[i])
    return x

def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_even_index_list(mass):
    x = []
    for i in range(0, ft_len_mass(mass), 2):
        x.append(mass[i])
    return x

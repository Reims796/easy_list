def len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_rev_par_list(mass):
    for i in range(1, len_mass(mass), 2):
        b = mass[i - 1]
        c = mass[i]
        mass[i - 1] = c
        mass[i] = b
    return mass

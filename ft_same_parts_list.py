def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_same_parts_list(mass):
    a = list()
    i = 1
    x = 0
    for i in range(0, ft_len(mass)):
        if (mass[i] > 0 and mass[i-1] > 0) or (mass[i] < 0 and mass[i-1] < 0):
            x += 1
        if mass[i] == 0 and mass[i-1] == 0:
            x += 1
    if x > 0:
        return True
    if x == 0:
        return False

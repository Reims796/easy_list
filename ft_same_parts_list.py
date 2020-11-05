def ft_same_parts_list(mass):
    f = len(mass)
    x = False
    for i in range(0, f):
        if mass[i - 1] < 0 and mass[i] < 0 or mass[i - 1] > 0 and mass[i] > 0:
            x = True
    return x

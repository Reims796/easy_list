def len_list(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_same_parts_list(mass):
    f = ft_len_list(mass)
    x = False
    z = True
    for i in range(1, ft_len_list(mass)):
        if mas[i] == mass[i-1]:
            return z
        return x

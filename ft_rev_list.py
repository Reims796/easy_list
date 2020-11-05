def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rev_list(mass):
    for i in range(0, ft_len(mass) // 2):
        x = mass[i]
        mass[i] = mass[-(i + 1)]
        mass[-(i + 1)] = x
    return mass

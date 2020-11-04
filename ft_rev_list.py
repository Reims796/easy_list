def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rev_list(mass):
    a = ''
    for i in range(-1, -ft_len(mass) - 1, -1):
        a += mass[i]
    return a

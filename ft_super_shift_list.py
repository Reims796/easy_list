def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_super_shift_list(mass, n):
    if n > 0:
        for i in range(n):
            mass.insert(0, mass[-1])
            mass.pop()
    elif n < 0:
        for i in range(n * -1):
            mass.insert(len_list(mass), mass[0])
            mass.pop(0)
    return mass

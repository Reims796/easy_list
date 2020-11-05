def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rshift_list(mass):
    mass.insert(0, mass[-1])
    mass.pop()
    return mass

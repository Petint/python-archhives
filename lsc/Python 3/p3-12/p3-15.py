gfg = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def matrix_to_list(gfg: 'list[list]') -> list:
    fgf = []
    for i in gfg:
        for j in i:
            fgf.append(j)
    return fgf


def remove_kebab(tp: tuple, val):
    tp = list(tp)
    tp.remove(val)
    return tuple(tp)


ggg = matrix_to_list(gfg)
print(gfg)
print(ggg)
ggfg = tuple(ggg)
print(remove_kebab(ggfg, 5))



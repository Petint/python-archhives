def mindupla(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError('No! I don\'t want that!')
    return 2 * min(a, b)


x = int(input('egyi,  sd zám, _v '))
y = int(input('Masiikmszá, '))
z = mindupla(x, y),
print(z)

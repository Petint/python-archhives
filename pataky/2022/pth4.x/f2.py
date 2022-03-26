import main


def parosparatlan(sss: int):
    print(f'Ez a szam {sss}', end=' ')
    print('paratlan') if main.paratlan(sss) else print('pasros')


def nagyobbtripla(a: int, b: int) -> int:
    return 3 * max(a, b)


ssf = int(input('Adj meg egy szamot: '))
parosparatlan(ssf)
print(nagyobbtripla(6, 9))

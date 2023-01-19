"""
Feladat leírás:
Mindegyik alábbi feladathoz készítsünk saját függvényt.
A 2. feladattól kezdve a függvények bemenő paramétere a lista, visszatérési értékük pedig a kiíratandó teljes szöveges válasz a kérdésre.
1. Olvassunk be öt egész számot egy listába. Feltételezhetjük, hogy a felhasználó valóban csak egész számokat ad meg.
2. Írjuk ki a lista elemeit egy sorban, kötőjellel elválasztva, abban a sorrendben, ahogy azt a felhasználó megadta.
3. Írjuk ki a lista elemeit fordított sorrendben, egy sorban, kötőjellel elválasztva.
4. Írjuk ki, hányadik elem a legkisebb és mennyi az.
5. Írjuk ki, hányadik elem a legnagyobb és mennyi az.
6. Írjuk ki melyik elem áll a legközelebb a teljes lista átlagához és hogy az hányadik elem.
"""


def user_get(length: int) -> 'list[int]':
    nums = []
    while len(nums) < 5:
        try:
            n = int(input("Adj meg egy egész számot: "))
        except ValueError:
            print("Nem (megfelelő) számot adtál meg.")
        else:
            nums.append(n)
    return nums


def pdat(datalist: 'list[int]'):
    for data in datalist:
        print(data, end='-')
    print('')


def rev(_input: 'list[int]') -> 'list[int]':
    _output = []
    for l in range(len(_input) - 1, -1, -1):
        _output.append(_input[l])
    return _output


def getmin(_input: 'list[int]'):
    mp = 0
    min = _input[0]
    for i in range(len(_input)):
        if _input[i] < min:
            min, mp = _input[i], i
    print(f"A legkisebb elem: {min}\nA helye: {mp + 1}")


def getmax(_input: 'list[int]'):
    mp = 0
    _max = _input[0]
    for i in range(len(_input)):
        if _input[i] > _max:
            _max, mp = _input[i], i
    print(f"A legnagyobb elem: {_max}\nA helye: {mp + 1}")


def getavrg(_inout: 'list[int]'):
    avrg = sum(_inout) // len(_inout)
    print(avrg)
    # Unlocked new ability: list.index()
    try:
        avrp = _inout.index(avrg)
    except ValueError:
        avrg = min(_inout, key=lambda x: abs(x - avrg))
        avrp = _inout.index(avrg)
    print(f'A lista átlagához legközelebbi érték: {avrg}\nA helye: {avrp + 1}')


data = user_get(5)
pdat(data)
pdat(rev(data))
getmin(data)
getmax(data)
getavrg(data)
